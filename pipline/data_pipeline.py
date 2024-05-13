import pandas as pd
import numpy as np
import os
from src.get_data import process_post
from src.clean_data import Clean_data
from src.feature_scale import Data_Feature_Scale
from model_dev.model_dev import Model_dev


def data_pipeline_func(credicts, movies):
    """
    This function is used to create the data pipeline for the model.
    :param credicts:
    :param movies:
    """
    data_df = process_post(movies, credicts)
    cleaned_data = Clean_data(data_df)
    main_data = Data_Feature_Scale(cleaned_data)
    similaritys = Model_dev(main_data, data_df)
    print(similaritys[0])
