import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from utils import Data_Save_File


class Feature_Scaling_Config:
    try:

        def __init__(self, data):
            self.data = data
            self.data_path = (
                "D:\my_projects\movie-recommendation-system\model\movies.pkl"
            )

        def Data_Merge(self):
            self.data["overview"] = self.data["overview"].apply(lambda x: [x])
            self.data["tags"] = (
                self.data["overview"]
                + self.data["genres"]
                + self.data["keywords"]
                + self.data["cast"]
                + self.data["crew"]
            )
            self.data["tags"] = self.data["tags"].apply(
                lambda x: " ".join(map(str, x)) if isinstance(x, list) else x
            )
            self.data["tags"] = self.data["tags"].astype(str)
            return self.data

        def Remove_Unknown_col(self):
            data2 = self.Data_Merge()
            data2.drop(
                ["overview", "genres", "keywords", "cast", "crew", "keywords"],
                axis=1,
                inplace=True,
            )

            return data2

        def Handle_Tags(self, tags_col):
            stemmer = PorterStemmer()
            tags_col = tags_col.lower()
            tags_col = tags_col.split()
            tags_col = [
                stemmer.stem(word)
                for word in tags_col
                if not word in set(stopwords.words("english"))
            ]
            tags_col = " ".join(tags_col)
            return tags_col

        def Feature_Scale_Configure(self):
            data2 = self.Remove_Unknown_col()
            data2["tags"] = data2["tags"].apply(self.Handle_Tags)
            return data2

        def Convert_Vector_func(self):
            data2 = self.Feature_Scale_Configure()
            Data_Save_File(data2, self.data_path)
            cv = CountVectorizer(max_features=500, stop_words="english")
            vector_data = cv.fit_transform(data2["tags"]).toarray()
            return vector_data

    except Exception as e:
        raise e


def Data_Feature_Scale(data_df):
    try:
        Feature_Scaling_Config_obj = Feature_Scaling_Config(data_df)
        main_data = Feature_Scaling_Config_obj.Convert_Vector_func()
        return main_data
    except Exception as e:
        raise e
