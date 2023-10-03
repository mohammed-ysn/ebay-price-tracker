import os
import pickle
from typing import Any


def dump(f_path: str, obj: Any) -> None:
    """Export an object to a file.

    Parameters
    ----------
    f_path : str
        The path to the file to be created.
    obj : Any
        The object to export.

    """
    with open(f_path, "wb") as f:
        pickle.dump(obj, f)


def load(f_path: str) -> Any:
    """Load an object from a file.

    Parameters
    ----------
    f_path : str
        The path to the object file.

    Returns
    -------
    Any
        The object.

    """
    with open(f_path, "rb") as f:
        return pickle.load(f)


def delete(f_path):
    """Delete a file.

    Parameters
    ----------
    f_path : str
        The path to the file to be deleted.

    """
    os.remove(f_path)
