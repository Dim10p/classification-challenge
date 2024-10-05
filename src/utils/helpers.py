import re
import pandas as pd

def convert_knn_indices_to_codes(clean_jobs,
                                 clean_labels,
                                 knn_indices):

    jobs_row_index_to_jobs_id = clean_jobs.id.to_dict()
    labels_row_index_to_taxonomy_id = clean_labels.code.to_dict()

    # Create dictionary for mapping of knn to jobs 
    dict_reslt = dict()
    for index, id in jobs_row_index_to_jobs_id.items():
        tmp = knn_indices[index]
        actual_job_id = [labels_row_index_to_taxonomy_id[x] for x in tmp]
        dict_reslt[id]=actual_job_id
    return dict_reslt


def extract_first_4_digit_string(text):
    # Define the regex pattern to match exactly 4 digits
    pattern = r'\d{4}'
    
    # Search for the first occurrence of the pattern
    match = re.search(pattern, text)
    
    # Check if a match is found
    if match:
        # Extract the matched string
        return match.group(0)
    else:
        return None