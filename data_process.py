import pandas as pd
import numpy as np
import os
from pipline.data_pipeline import data_pipeline_func

data_path_1 = r"data/tmdb_5000_credits.csv"
data_path_2 = r"data/tmdb_5000_movies.csv"

data_pipeline_func(data_path_1, data_path_2)
