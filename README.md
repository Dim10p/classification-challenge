# WEB INTELLIGENCE - CLASSIFICATION CHALLENGE - Organized by European Statistics Awards

## Team Composition
•	**Dimitrios Petridis:** Data Scientist, European Central Bank, dimitris.petridis@ecb.europa.eu <br>
•	**Georgios Kanellos:** Team Lead Statistics, European Central Bank, georgios.kanellos@ecb.europa.eu <br>
•	**Jannic Cutura:** Senior Data Engineer, European Central Bank & Research Fellow, DSTI School of Engineering, jannic.cutura@dsti.institute

## Solution

In this project we solve the classification challenge posed by Eurostat in the 2024 Web Intelligence data science competition. Our strategy leverages a combination of RAG and prompt engineering: After pre-processing the dataset, we create embeddings of job descriptions and taxonomy. To avoid the curse of dimensionality we identify the k-nearest-neighbors between each job advertisement and all taxonomy labels. The k candidate solutions are further scrutinized using a large-language model to yield the four-digit taxonomy code. 

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
