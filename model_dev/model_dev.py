import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from utils import Data_Save_File
import pickle


def Model_dev(data_main_arr, data):
    try:
        data_path = "D:\my_projects\movie-recommendation-system\model\similaritys.pkl"
        similaritys = cosine_similarity(data_main_arr)
        Data_Save_File(similaritys, data_path)
        # user_input = str(input("Enter Movie: "))
        # index_val = data[data["title"] == user_input].index[0]
        # suggestions = sorted(
        #     list(enumerate(similaritys[index_val])), reverse=True, key=lambda x: x[1]
        # )
        # for i in suggestions[:5]:
        #     movie_title = data["title"].iloc[i[0]]
        #     print(movie_title)
        with open(data_path, "rb") as f:
            similaritys = pickle.load(f)
        return similaritys
    except Exception as e:
        print("Error Generated in {}".format(e))
        raise e
