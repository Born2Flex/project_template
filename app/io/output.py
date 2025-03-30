def print_to_console(text):
    """
    Print text to the console.

    Args:
        text (str): Text for printing.
    """
    print(text)


def write_to_file(text, file_path):
    """
    Write text to the specified file.

    Args:
        text (str): Text to be written.
        file_path (str): Path to the file.
    """
    with open(file_path, "w") as file:
        file.write(text)
