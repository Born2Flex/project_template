import unittest
import pandas as pd
from app.io.input import read_text_from_file, read_text_from_file_with_pandas


class TestInputOperations(unittest.TestCase):

    def test_read_text_from_file_normal(self):
        # Arrange
        file_path = 'data/test_text.txt'
        expected_content = 'Hello World'

        # Act
        result = read_text_from_file(file_path)

        # Assert
        self.assertEqual(result, expected_content)

    def test_read_text_from_file_empty(self):
        # Arrange
        file_path = 'data/empty_text.txt'
        expected_content = ''

        # Act
        result = read_text_from_file(file_path)

        # Assert
        self.assertEqual(result, expected_content)

    def test_read_text_from_file_not_found(self):
        # Arrange
        file_path = 'nonexistent.txt'

        # Act & Assert
        with self.assertRaises(FileNotFoundError):
            read_text_from_file(file_path)

    def test_read_text_from_file_with_pandas_normal(self):
        # Arrange
        file_path = 'data/test.csv'
        expected_content = "col1 col2\n  a   1\n  b   2"

        # Act
        result = read_text_from_file_with_pandas(file_path).replace('  ', ' ').strip()

        # Assert
        self.assertEqual(result, expected_content)

    def test_read_text_from_file_with_pandas_empty(self):
        # Arrange
        file_path = 'data/empty.csv'

        # Act & Assert
        with self.assertRaises(pd.errors.EmptyDataError):
            read_text_from_file_with_pandas(file_path)

    def test_read_text_from_file_with_pandas_not_found(self):
        # Arrange
        file_path = 'nonexistent.csv'

        # Act & Assert
        with self.assertRaises(FileNotFoundError):
            read_text_from_file_with_pandas(file_path)


if __name__ == '__main__':
    unittest.main()
