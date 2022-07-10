import os
import pickle


def dump(f_path, obj):
    with open(f_path, "wb") as f:
        pickle.dump(obj, f)


def load(f_path):
    with open(f_path, "rb") as f:
        return pickle.load(f)


def remove(f_path):
    os.remove(f_path)
