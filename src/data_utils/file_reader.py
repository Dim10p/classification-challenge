import pandas as pd
from src.utils.constants import Paths


class FileReader:

    @classmethod
    def read_job_advertisements(cls) -> pd.DataFrame:
        print("Reading raw job advertisements from:", Paths.INPUT_DATA_PATH)
        df = pd.read_csv(Paths.INPUT_DATA_PATH,
                         engine='python',
                         encoding='utf-8')
        df = df.convert_dtypes()
        print("Raw job advertisements read successfully. Shape:", df.shape)
        return df

    @classmethod
    def read_clean_job_advertisements(cls) -> pd.DataFrame:
        print("Reading clean job advertisements from:", Paths.CLEAN_DATA_PATH)
        df = pd.read_csv(Paths.CLEAN_DATA_PATH,
                         engine='python',
                         encoding='utf-8')
        df = df.convert_dtypes()
        print("Clean job advertisements read successfully. Shape:", df.shape)
        return df

    @classmethod
    def read_isco_labels(cls) -> pd.DataFrame:
        print("Reading raw ISCO taxonomy from:", Paths.INPUT_LABELS_PATH)
        df = pd.read_csv(Paths.INPUT_LABELS_PATH,
                         engine='python',
                         encoding='utf-8',
                         dtype={'code': str})
        df = df.drop('isco_uri', axis=1).rename(columns={'label': 'title'}).convert_dtypes()
        print("Raw eurostat taxonomy read successfully. Shape:", df.shape)
        return df
    
    @classmethod
    def read_external_labels(cls) -> pd.DataFrame:
        print("Reading reference taxonomy from:", Paths.INPUT_TAXONOMY_PATH)
        df = (pd.read_excel(Paths.INPUT_TAXONOMY_PATH,
                            dtype={'ISCO 08 Code': str})
              .rename(columns={'ISCO 08 Code': 'code',
                               'Notes': 'notes',
                               'Title EN': 'title_ext',
                               'Tasks include': 'tasks_include',
                               'Included occupations': 'included_occupations',
                               'Excluded occupations': 'excluded_occupations',
                               'Definition': 'description_ext',
                               'Level': 'level'})
              )
        print("Reference taxonomy read and processed successfully. Shape:", df.shape)
        return df

    @classmethod
    def read_combined_labels(cls) -> pd.DataFrame:
        reference = cls.read_external_labels()
        eurostat = cls.read_isco_labels()
        print("Merging reference taxonomy and eurostat taxonomy...")
        df = reference.merge(eurostat,
                             on="code",
                             how="inner")
        print("Taxonomies merged successfully. Shape:", df.shape)
        df = df[
            ['code',
             'title',
             'description',
             'title_ext',
             'description_ext',
             'level',
             'tasks_include',
             'included_occupations',
             'excluded_occupations',
             'notes']]
        print("Combined taxonomy read and enhanced successfully. Shape:", df.shape)
        return df

