import os
import pickle
from typing import Any


def dump(f_path: str, obj: Any) -> None:
    """Dump an object to a pickle file."""
    with open(f_path, "wb") as f:
        pickle.dump(obj, f)


def load(f_path: str) -> Any:
    """Load an object from a file."""
    with open(f_path, "rb") as f:
        return pickle.load(f)


def delete(f_path):
    """Delete a file."""
    os.remove(f_path)
