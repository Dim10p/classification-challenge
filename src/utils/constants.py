import os
from pathlib import Path
from dataclasses import dataclass


class Paths:
    _current_file_path = Path(os.path.abspath(__name__))
    ROOT_PATH = _current_file_path.parent

    DATA_PATH = Path(ROOT_PATH, "data")

    RAW_DATA_PATH = Path(DATA_PATH, "raw")
    INTERIM_DATA_PATH = Path(DATA_PATH, "interim")
    EMBEDDINGS_DATA_PATH = Path(DATA_PATH, "embeddings")
    SUBMISSION_DATA_PATH = Path(DATA_PATH, "submission")

    INPUT_DATA_PATH = Path(RAW_DATA_PATH, "wi_dataset.csv")
    INPUT_LABELS_PATH = Path(RAW_DATA_PATH, "wi_labels.csv")
    INPUT_TAXONOMY_PATH = Path(RAW_DATA_PATH, "ISCO-08 EN Structure and definitions.xlsx")

    CLEAN_DATA_PATH = Path(INTERIM_DATA_PATH, "wi_dataset_clean.csv")
    CLEAN_LABELS_PATH = Path(INTERIM_DATA_PATH, "wi_labels_clean.csv")

    SOURCE_PATH = Path(ROOT_PATH, "src")

    UTILS_PATH = Path(SOURCE_PATH, "utils")

    DATA_UTILS_PATH = Path(SOURCE_PATH, "data_utils")

