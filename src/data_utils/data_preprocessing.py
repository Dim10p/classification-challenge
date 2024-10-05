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
                                             contains_only_punctuations_regex)

warnings.simplefilter(action='ignore', category=FutureWarning)


def clean_job_advertisements(
        df: pd.DataFrame,
        desc_convert_html_to_ascii: bool = True,
        desc_remove_html_tags: bool = True,
        desc_split_uppercase: bool = True,
        desc_convert_to_lowercase: bool = True,
        desc_remove_whitespaces: bool = True,
        desc_remove_repeated_punctuations: bool = True,
        desc_remove_only_punctuations: bool = True,
        desc_remove_numbers: bool = True,
        title_convert_html_to_ascii: bool = True,
        title_remove_html_tags: bool = True,
        title_split_uppercase: bool = True,
        title_convert_to_lowercase: bool = True,
        title_remove_whitespaces: bool = True,
        title_remove_repeated_punctuations: bool = True,
        title_remove_only_punctuations: bool = True,
        title_remove_numbers: bool = True,) -> pd.DataFrame:
    """
    Cleans the job advertisements DataFrame by applying a series of text cleaning operations.

    Args:
        df (pd.DataFrame): The DataFrame containing job advertisements data.
        desc_convert_html_to_ascii (bool): Convert HTML entities to ASCII in the description.
        desc_remove_html_tags (bool): Remove HTML tags from the description.
        desc_split_uppercase (bool): Split uppercase characters following lowercase characters in the description.
        desc_convert_to_lowercase (bool): Convert the description to lowercase characters.
        desc_remove_whitespaces (bool): Remove extra whitespaces from the description.
        desc_remove_repeated_punctuations (bool): Remove repeated punctuations from the description.
        desc_remove_only_punctuations (bool): Convert the desc to '-' if it contains only punctuations.
        desc_remove_numbers (bool): Remove misleading numbers from job description.
        title_convert_html_to_ascii (bool): Convert HTML entities to ASCII in the title.
        title_remove_html_tags (bool): Remove HTML tags from the title.
        title_split_uppercase (bool): Split uppercase characters following lowercase characters in the title.
        title_convert_to_lowercase (bool): Convert the title to lowercase.
        title_remove_whitespaces (bool): Remove extra whitespaces from the title.
        title_remove_repeated_punctuations (bool): Whether to remove repeated punctuations from the title.
        title_remove_only_punctuations (bool): Convert the title to '-' if it contains only punctuations.
        title_remove_numbers (bool): Remove misleading numbers from job title.

    Returns:
        pd.DataFrame: Cleaned DataFrame with the specified operations applied.

    """
    print("Starting cleaning job advertisements...")

    # Convert data types
    df = df.convert_dtypes()

    # Count and report missing values
    id_na_count = df.id.isna().sum()
    title_na_count = df.title.isna().sum()
    description_na_count = df.description.isna().sum()

    print(f"Number of missing values in id: {id_na_count}")
    print(f"Number of missing values in title: {title_na_count}")
    print(f"Number of missing values in description: {description_na_count}")

    # Replace missing values with empty string
    df['title'] = df['title'].fillna("-")
    df['description'] = df['description'].fillna("-")

    print(f"Replaced {title_na_count} missing values in title with '-'.")
    print(f"Replaced {description_na_count} missing values in description with '-'.")

    # Convert data types
    print("Data types after filling missing values:")
    print(df.dtypes)

    # Clean description column
    print("Cleaning description column...")

    # Create clean description column
    df['description_clean'] = df['description']

    if desc_convert_html_to_ascii:
        # Convert html to ascii in description
        print("Converting HTML entities to ASCII in description...")
        df['description_clean'] = df['description'].apply(convert_html_to_ascii)
    if desc_remove_html_tags:
        # Remove html tags from descriptions
        print("Removing HTML tags from description...")
        df['description_clean'] = df['description_clean'].apply(remove_html_tags)
    if desc_split_uppercase:
        # Split uppercase characters after lowercase characters in description
        print("Splitting uppercase characters after lowercase in description...")
        df['description_clean'] = df['description_clean'].apply(split_uppercase_after_lowercase)
    if desc_convert_to_lowercase:
        # Convert description to lowercase
        print("Converting description to lowercase...")
        df['description_clean'] = df['description_clean'].apply(convert_to_lowercase)
    if desc_remove_whitespaces:
        # Remove extra whitespaces from description
        print("Removing extra whitespaces from description...")
        df['description_clean'] = df['description_clean'].apply(remove_whitespaces)
    if desc_remove_repeated_punctuations:
        # Remove repeated punctuations from description
        print("Removing repeated punctuations from description...")
        df['description_clean'] = df['description_clean'].apply(remove_repeated_punctuations)
    if desc_remove_only_punctuations:
        # Convert description to empty string when it contains only punctuations
        print("Converting description to empty string when it contains only punctuations...")
        df['description_clean'] = df['description_clean'].apply(
            lambda x: "-" if contains_only_punctuations_regex(x) else x)
    if desc_remove_numbers:
        # Removing misleading numbers from job description
        print("Removing misleading numbers from job description...")
        df['description_clean_nn'] = df['description_clean'].str.replace(r'\d+', '', regex=True)

    # Clean title column
    print("Cleaning title column...")

    # Create clean title column
    df['title_clean'] = df['title']

    if title_convert_html_to_ascii:
        # Convert html to ascii in title
        print("Converting HTML entities to ASCII in title...")
        df['title_clean'] = df['title'].apply(convert_html_to_ascii)
    if title_remove_html_tags:
        # Remove html tags from title
        print("Removing HTML tags from title...")
        df['title_clean'] = df['title_clean'].apply(remove_html_tags)
    if title_split_uppercase:
        # Split uppercase characters after lowercase characters in title
        print("Splitting uppercase characters after lowercase in title...")
        df['title_clean'] = df['title_clean'].apply(split_uppercase_after_lowercase)
    if title_convert_to_lowercase:
        # Convert title to lowercase
        print("Converting title to lowercase...")
        df['title_clean'] = df['title_clean'].apply(convert_to_lowercase)
    if title_remove_whitespaces:
        # Remove extra whitespaces from title
        print("Removing extra whitespaces from title...")
        df['title_clean'] = df['title_clean'].apply(remove_whitespaces)
    if title_remove_repeated_punctuations:
        # Remove repeated punctuations from title
        print("Removing repeated punctuations from title...")
        df['title_clean'] = df['title_clean'].apply(remove_repeated_punctuations)
    if title_remove_only_punctuations:
        # Convert title to empty string when it contains only punctuations
        print("Converting title to empty string when it contains only punctuations...")
        df['title_clean'] = df['title_clean'].apply(
            lambda x: "-" if contains_only_punctuations_regex(x) else x)
    if title_remove_numbers:
        # Removing misleading numbers from job titles
        print("Removing misleading numbers from job titles...")
        df['title_clean_nn'] = df['title_clean'].str.replace(r'\d+', '', regex=True)


    print("Completed cleaning job advertisements.")

    # Convert data types
    df = df.convert_dtypes()
    print("Final data types:")
    print(df.dtypes)

    return df
