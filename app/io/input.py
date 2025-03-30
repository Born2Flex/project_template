# input.py
import pandas as pd


def read_from_console():
    """
       Read text from console.

       Returns:
           str: Text entered from the console.
       """
    txt = input("Enter text: ")
    return txt


def read_text_from_file(file_path):
    """
    Read text from file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Content of the file.
    """
    with open(file_path, "r") as file:
        return file.read()


def read_text_from_file_with_pandas(file_path):
    """
    Read data from a csv file via pandas library.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Content of the file.
    """
    data = pd.read_csv(file_path)
    return data.to_string(index=False)
