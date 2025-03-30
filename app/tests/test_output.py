import os
import unittest
from app.io.output import write_to_file


class TestOutputOperations(unittest.TestCase):
    def test_write_to_file_normal(self):
        # Arrange
        file_path = 'data/test_write.txt'
        test_content = 'Writing test successful'

        # Act
        write_to_file(test_content, file_path)

        # Assert
        with open(file_path, 'r') as file:
            result = file.read()
        self.assertEqual(result, test_content)
        os.remove(file_path)

    def test_write_to_file_empty(self):
        # Arrange
        file_path = 'data/test_write_empty.txt'
        test_content = ''

        # Act
        write_to_file(test_content, file_path)

        # Assert
        with open(file_path, 'r') as file:
            result = file.read()
        self.assertEqual(result, test_content)
        os.remove(file_path)

    def test_write_to_file_overwrite(self):
        # Arrange
        file_path = 'data/test_write_overwrite.txt'
        initial_content = 'Initial content'
        overwrite_content = 'Overwrite content'

        # Act
        write_to_file(initial_content, file_path)
        write_to_file(overwrite_content, file_path)

        # Assert
        with open(file_path, 'r') as file:
            result = file.read()
        self.assertEqual(result, overwrite_content)
        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
