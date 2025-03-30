# main.py
from app.io.input import read_from_console, read_text_from_file, read_text_from_file_with_pandas
from app.io.output import print_to_console, write_to_file


def main():
    user_input = read_from_console()
    print_to_console("You entered: " + user_input)
    write_to_file(user_input, "data/output.txt")

    file_content = read_text_from_file("data/somefile.txt")
    print_to_console("File content: " + file_content)
    write_to_file(file_content, "data/output.txt")

    df_content = read_text_from_file_with_pandas("data/somefile.csv").to_string()
    print_to_console("DataFrame content:\n" + df_content)
    write_to_file(df_content, "data/output.txt")


if __name__ == '__main__':
    main()
