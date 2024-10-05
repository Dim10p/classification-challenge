import pandas as pd
from typing import List, Dict, Tuple
from tqdm import tqdm
import ollama


def generate_prompts(
    clean_jobs: pd.DataFrame,
    clean_labels: pd.DataFrame,
    dict_reslt: Dict[int, List[str]],
    system_template: str,
    user_template: str
    ) -> Dict[int, Tuple[str, str]]:
    """
    Generate prompts for job classification based on job descriptions and labels.
    
    Parameters:
    clean_jobs (pd.DataFrame): DataFrame containing job information
    clean_labels (pd.DataFrame): DataFrame containing label information
    dict_reslt (Dict[int, List[str]]): Dictionary mapping job IDs to lists of label codes.
    system_template (str): Template for the system content.
    user_template (str): Template for the user content.
    
    Returns:
    Dict[int, Tuple[str, str]]: Dictionary mapping job IDs to tuples containing SYSTEM and USER prompts.
    """
    prompts = {}
    
    # Use tqdm to monitor progress
    for job_id, label_indices in tqdm(dict_reslt.items(), desc="Generating prompts"):
        # Using boolean indexing to filter the clean_jobs DataFrame
        job_row = clean_jobs[clean_jobs['id'] == job_id]
        job_title = job_row['title_clean'].values[0]
        job_desc = job_row['description_clean'].values[0]
        
        choices = []
        for label_id in label_indices:
            # Using boolean indexing to filter the clean_labels DataFrame
            label_row = clean_labels[clean_labels['code'] == label_id]
            choice = (
                f"ID: {label_row['code'].values[0]}\n"
                f"TITLE: {label_row['title_ext_level_4_clean'].values[0]}\n"
                f"DESCRIPTION: {label_row['description_ext_level_4_clean'].values[0]}\n"
                f"TASKS INCLUDE: {label_row['tasks_include_level_4_clean'].values[0]}\n"
                f"INCLUDED OCCUPATIONS: {label_row['included_occupations_level_4_clean'].values[0]}"
            )
            choices.append(choice)
        
        choices_str = '\n|||\n'.join(choices)
        all_ids = ', '.join(label_indices)
        
        system_content = system_template.format(choices_str, all_ids)
        user_content = user_template.format(job_title, job_desc)
        
        prompts[job_id] = (system_content, user_content)
    
    return prompts
