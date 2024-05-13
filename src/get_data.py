import pandas as pd
import numpy as np
import os


class Data_Ingestion_Config:
    def __init__(self, data_path1, data_path2) -> pd.DataFrame:
        self.data_path1 = data_path1
        self.data_path2 = data_path2

    def Data_Merge(self):
        data_df_1 = pd.read_csv(self.data_path1)
        data_df_2 = pd.read_csv(self.data_path2)
        data_df_2 = data_df_2.merge(data_df_1)
        return data_df_2


def process_post(movies, credicts) -> pd.DataFrame:
    Data_Ingestion_Config_obj = Data_Ingestion_Config(movies, credicts)
    data_df = Data_Ingestion_Config_obj.Data_Merge()
    return data_df
