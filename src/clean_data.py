import numpy as np
import os
import ast
import warnings
import pandas as pd

warnings.filterwarnings("ignore")


class Data_Cleaning_Config:
    def __init__(self, data):
        self.data = data

    def Data_Collection_func(self):
        main_data = self.data[
            ["movie_id", "title", "cast", "crew", "genres", "keywords", "overview"]
        ]
        return main_data

    def data_Genres(self, genres):
        for i in ast.literal_eval(genres):
            return [i["name"]]

    def data_cast(self, cast):
        char_list = []
        count = 0
        for i in ast.literal_eval(cast):
            if count < 5:
                char_list.append(i["name"])
                count += 1
            else:
                break
        return char_list

    def data_director(self, director):
        for i in ast.literal_eval(director):
            if i["department"] == "Directing":
                return [i["name"]]

    def data_keywords(self, keywords):
        for i in ast.literal_eval(keywords):
            return [i["name"]]

    def Data_Cleaning_Column_func(self) -> pd.DataFrame:
        try:
            self.main_data1 = self.Data_Collection_func()
            self.main_data1["genres"] = self.main_data1["genres"].apply(
                self.data_Genres
            )
            self.main_data1["cast"] = self.main_data1["cast"].apply(self.data_cast)
            self.main_data1["crew"] = self.main_data1["crew"].apply(self.data_director)
            self.main_data1["keywords"] = self.main_data1["keywords"].apply(
                self.data_keywords
            )
            return self.main_data1

        except Exception as e:
            print("Error Generated in {}".format(e))
            raise e


def Clean_data(data) -> pd.DataFrame:
    try:
        Data_Cleaning_Config_obj = Data_Cleaning_Config(data)
        cleaned_data = Data_Cleaning_Config_obj.Data_Cleaning_Column_func()
        return cleaned_data
    except Exception as e:
        print("Error Generated in {}".format(e))
        raise e
