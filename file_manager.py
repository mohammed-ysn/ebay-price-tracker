import pickle


class FileManager:
    @staticmethod
    def dump(f_path, obj):
        with open(f_path, "wb") as f:
            pickle.dump(obj, f)

    @staticmethod
    def load(f_path):
        with open(f_path, "rb") as f:
            return pickle.load(f)
