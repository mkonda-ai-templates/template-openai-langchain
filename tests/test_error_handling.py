import unittest
from unittest.mock import patch
from src.app import ask_llm

class TestErrorHandling(unittest.TestCase):

    @patch('builtins.print')
    def test_ask_llm_error_handling(self, mock_print):
        with self.assertRaises(ValueError) as context:
            ask_llm("")
        self.assertIsInstance(context.exception, ValueError)

if __name__ == '__main__':
    unittest.main()