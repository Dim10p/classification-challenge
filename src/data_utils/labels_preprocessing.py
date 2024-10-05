import pandas as pd
import warnings

from src.data_utils.file_reader import FileReader
from src.utils.constants import Paths
from src.utils.preprocessing_helpers import (convert_html_to_ascii,
                                             remove_html_tags,
                                             split_uppercase_after_lowercase,
                                             convert_to_lowercase,
                                             remove_whitespaces,
                                             remove_repeated_punctuations,
                                             contains_only_punctuations_regex,
                                             extract_included_occupations,
                                             extract_excluded_numbers)

warnings.simplefilter(action='ignore', category=FutureWarning)


def merge_taxonomies(taxonomy: pd.DataFrame, labels: pd.DataFrame):
    """
    Merges the taxonomy and labels dataframes and enhances the taxonomy with higher-level information.
    
    Parameters:
    - taxonomy: pd.DataFrame, ISCO-08 taxonomy dataframe 
    - labels: pd.DataFrame, Eurostat taxonomy labels dataframe
    
    Returns:
    - df: pd.DataFrame, the merged and enhanced dataframe
    """
    print("Merging reference taxonomy and eurostat taxonomy...")
    
    # Perform an inner join to keep only the 436 categories
    df = taxonomy.merge(labels, on='code', how='inner', suffixes=('', '_level_4'))
    df = df.drop(['level'], axis=1)
    df = df.rename(columns={
        'title_ext': 'title_ext_level_4', 
        'description_ext': 'description_ext_level_4', 
        'tasks_include': 'tasks_include_level_4', 
        'included_occupations': 'included_occupations_level_4', 
        'excluded_occupations': 'excluded_occupations_level_4', 
        'notes': 'notes_level_4'
    })
    
    # Extract higher-level information
    df['MajorGroup'] = df['code'].str[:1]
    df['SubMajorGroup'] = df['code'].str[:2]
    df['MinorGroup'] = df['code'].str[:3]
    
    # Ensure the higher-level information dataframes are correct
    major_info = taxonomy[taxonomy['code'].str.len() == 1].set_index('code')
    sub_major_info = taxonomy[taxonomy['code'].str.len() == 2].set_index('code')
    minor_info = taxonomy[taxonomy['code'].str.len() == 3].set_index('code')
    
    # Rename columns in higher-level dataframes to avoid conflicts
    major_info = major_info.add_suffix('_level_1')
    sub_major_info = sub_major_info.add_suffix('_level_2')
    minor_info = minor_info.add_suffix('_level_3')
    
    # Perform the joins
    df = df.join(major_info, on='MajorGroup')
    df = df.join(sub_major_info, on='SubMajorGroup')
    df = df.join(minor_info, on='MinorGroup')
    
    df = df.drop(['level_level_3', 'level_level_2', 'level_level_1', 'MajorGroup', 'SubMajorGroup', 'MinorGroup'], axis=1)
    
    print("Taxonomies merged successfully. Shape:", df.shape)
    print("Combined taxonomy (boosted) read and enhanced successfully. Shape:", df.shape)
    
    return df

def clean_isco_labels(
    df: pd.DataFrame,
    all_convert_html_to_ascii: bool = True,
    all_remove_html_tags: bool = True,
    all_split_uppercase: bool = True,
    all_convert_to_lowercase: bool = True,
    all_remove_whitespaces: bool = True,
    all_remove_repeated_punctuations: bool = True,
    all_remove_only_punctuations: bool = True
) -> pd.DataFrame:
    """
    Cleans the specified columns in the DataFrame by applying a series of text cleaning operations.
    
    Args:
        df (pd.DataFrame): The DataFrame containing ISCO labels.
        all_convert_html_to_ascii (bool): Convert HTML entities to ASCII.
        all_remove_html_tags (bool): Remove HTML tags.
        all_split_uppercase (bool): Split uppercase characters following lowercase characters.
        all_convert_to_lowercase (bool): Convert to lowercase characters.
        all_remove_whitespaces (bool): Remove extra whitespaces.
        all_remove_repeated_punctuations (bool): Remove repeated punctuations.
        all_remove_only_punctuations (bool): Convert to '-' if it contains only punctuations.
    
    Returns:
        pd.DataFrame: Cleaned DataFrame with the specified operations applied.
    """
    print("Starting cleaning isco labels...")

    # Convert data types
    df = df.convert_dtypes()

    # Count and report missing values
    for col in df.columns:
        na_count = df[col].isna().sum()
        print(f"Number of missing values in {col}: {na_count}")
        # Replace missing values with empty string
        df[col] = df[col].fillna('-')
        print(f"Replaced {na_count} missing values in {col} with '-'.")

    # Convert data types again after filling missing values
    print("Data types after filling missing values:")
    print(df.dtypes)

    # Extract included occupations to a new column
    print("Extracting included occupations...")
    df['included_occupations_map'] = df['description'].apply(extract_included_occupations)

    # Extract excluded occupations to a new column
    print("Extracting excluded occupations...")
    df['excluded_occupations_map'] = df['description'].apply(extract_excluded_numbers)

    # Apply cleaning operations to all columns
    for col in ['title_ext_level_4', 'description_ext_level_4',
       'tasks_include_level_4', 'included_occupations_level_4',
       'excluded_occupations_level_4', 'notes_level_4', 'title_ext_level_1',
       'description_ext_level_1', 'tasks_include_level_1',
       'included_occupations_level_1', 'excluded_occupations_level_1',
       'notes_level_1', 'title_ext_level_2', 'description_ext_level_2',
       'tasks_include_level_2', 'included_occupations_level_2',
       'excluded_occupations_level_2', 'notes_level_2', 'title_ext_level_3',
       'description_ext_level_3', 'tasks_include_level_3',
       'included_occupations_level_3', 'excluded_occupations_level_3',
       'notes_level_3']:
        print(f"Cleaning column: {col}")
        df[f'{col}_clean'] = df[col]
        
        if all_convert_html_to_ascii:
            print(f"Converting HTML entities to ASCII in {col}...")
            df[f'{col}_clean'] = df[f'{col}_clean'].apply(convert_html_to_ascii)
        
        if all_remove_html_tags:
            print(f"Removing HTML tags from {col}...")
            df[f'{col}_clean'] = df[f'{col}_clean'].apply(remove_html_tags)
        
        if all_split_uppercase:
            print(f"Splitting uppercase characters after lowercase in {col}...")
            df[f'{col}_clean'] = df[f'{col}_clean'].apply(split_uppercase_after_lowercase)
        
        if all_convert_to_lowercase:
            print(f"Converting {col} to lowercase...")
            df[f'{col}_clean'] = df[f'{col}_clean'].apply(convert_to_lowercase)
        
        if all_remove_whitespaces:
            print(f"Removing extra whitespaces from {col}...")
            df[f'{col}_clean'] = df[f'{col}_clean'].apply(remove_whitespaces)
        
        if all_remove_repeated_punctuations:
            print(f"Removing repeated punctuations from {col}...")
            df[f'{col}_clean'] = df[f'{col}_clean'].apply(remove_repeated_punctuations)
        
        if all_remove_only_punctuations:
            print(f"Converting {col} to empty string when it contains only punctuations...")
            df[f'{col}_clean'] = df[f'{col}_clean'].apply(
                lambda x: '-' if contains_only_punctuations_regex(x) else x
            )

    # Creating unique id column
    print("Creating unique id column...")
    df["id"] = (df.index + 1).astype("int64")

    # Convert data types
    df = df.convert_dtypes()
    print("Final data types:")
    print(df.dtypes)

    return df
    
