# WEB INTELLIGENCE - CLASSIFICATION CHALLENGE - Organized by European Statistics Awards


## Overview
In the area of Web Intelligence, the European Statistics Awards Programme aims to discover promising methodologies for processing content from the World Wide Web to extract valuable data for statistical and analytical purposes.

The European Statistics Awards **Web Intelligence Classification of Occupations for Online Job Advertisements Challenge (WI Classification Challenge)** focuses on developing approaches that learn how to assign a class label (from the known taxonomy) to job advertisements from a given dataset.

## Description of the Classification of Occupations for Online Job Advertisements Challenge
An online job advertisement (OJA) is information posted online about a job opening targeted at potential job-seeking applicants. Online job advertisements are usually published on job posting websites, company websites, and portals for job seekers. They typically contain a job description, information about the hiring company, job benefits, and requirements for job seekers.

To calculate meaningful statistics, occupational class labels are provided for online job advertisement entries. Given the data collection method and the size of the online job advertisements datasets, an efficient and robust automated solution is needed for this purpose.

The goal of the **Classification of Occupations for Online Job Advertisements Challenge** is to develop approaches that learn how to assign a class label (from the known taxonomy) to job advertisements from a given job ads dataset.

The International Standard Classification of Occupations (ISCO) is a four-level classification of occupation groups managed by the International Labour Organisation (ILO). Its structure follows a grouping by education level.

Participants will obtain a multilingual dataset of job advertisements with the following fields:
- job posting id
- job title
- job description

Participants are required to use the provided version of the ISCO taxonomy for target classes. To download the job advertisements and ISCO taxonomy labels, navigate to: **Participate > Files** and click on the **Public Data** button. This will download the zip file with the `wi_dataset.csv`, containing the job advertisements examples, and the `wi_labels.csv` file, which contains the ISCO taxonomy.

The evaluation will be performed on a gold standard dataset (a subset of the original multilingual dataset of job advertisements) which will not be shared with participants.

## The Competition Dataset
The competition dataset contains 26k online job advertisements (OJA), retrieved from around 400 websites active in the European Union, which have been anonymised for the purposes of the competition (any reference to personal data).

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


