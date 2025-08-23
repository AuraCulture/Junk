import unittest
from junk.cli import main
from unittest.mock import patch, MagicMock
import sys

class TestCLI(unittest.TestCase):

    @patch('junk.cli.cleanup')
    def test_main_success(self, mock_cleanup):
        mock_cleanup.return_value = True
        with patch('sys.exit') as mock_exit:
            main()
            mock_exit.assert_called_once_with(0)

    @patch('junk.cli.cleanup')
    def test_main_failure(self, mock_cleanup):
        mock_cleanup.return_value = False
        with patch('sys.exit') as mock_exit:
            main()
            mock_exit.assert_called_once_with(1)

    @patch('builtins.input', side_effect=['y'])
    def test_confirm_cleanup(self, mock_input):
        with patch('junk.cli.cleanup') as mock_cleanup:
            mock_cleanup.return_value = True
            result = main()
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['n'])
    def test_cancel_cleanup(self, mock_input):
        with patch('junk.cli.cleanup') as mock_cleanup:
            result = main()
            self.assertIsNone(result)
            mock_cleanup.assert_not_called()

if __name__ == '__main__':
    unittest.main()
