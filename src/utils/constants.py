"""
This file contains all the constants that are used in this project.
"""

import os


class Directories:
    DATA_DIR = "data"
    EXTERNAL_DATA_DIR = os.path.join(DATA_DIR, "external")
    INTERIM_DATA_DIR = os.path.join(DATA_DIR, "interim")
    PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
    RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")


class FilePaths:
    MAKEFILE = "Makefile"
    README = "README.md"
    LICENSE = "LICENSE"
    REQUIREMENTS = "requirements.txt"
    SETUP_PY = "setup.py"
    TOX_INI = "tox.ini"


class SourceCode:
    SRC_DIR = "src"
    DATA_SCRIPTS_DIR = os.path.join(SRC_DIR, "data")
    FEATURES_SCRIPTS_DIR = os.path.join(SRC_DIR, "features")
    MODELS_SCRIPTS_DIR = os.path.join(SRC_DIR, "models")
    UTILS_SCRIPTS_DIR = os.path.join(SRC_DIR, "utils")
    VISUALIZATION_SCRIPTS_DIR = os.path.join(SRC_DIR, "visualization")


class Notebooks:
    NOTEBOOKS_DIR = "notebooks"


class Reports:
    REPORTS_DIR = "reports"
    FIGURES_DIR = os.path.join(REPORTS_DIR, "figures")


class Models:
    MODELS_DIR = "models"


class Docs:
    DOCS_DIR = "docs"


class References:
    REFERENCES_DIR = "references"
