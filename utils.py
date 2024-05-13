import os
import pickle


def Data_Save_File(filename, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(filename, f)
