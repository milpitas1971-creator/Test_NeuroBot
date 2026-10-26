"""Unit tests for the add_two_numbers.py command-line script."""

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("add_two_numbers.py")


class AddTwoNumbersTests(unittest.TestCase):
    def test_adds_input_numbers(self):
        test_cases = (
            ("2\n3\n", "Sum: 5.0"),
            ("2.5\n1.25\n", "Sum: 3.75"),
            ("-3\n1\n", "Sum: -2.0"),
        )

        for user_input, expected_sum in test_cases:
            with self.subTest(user_input=user_input):
                result = subprocess.run(
                    [sys.executable, str(SCRIPT_PATH)],
                    input=user_input,
                    capture_output=True,
                    text=True,
                    check=True,
                )
                self.assertTrue(result.stdout.rstrip().endswith(expected_sum))


if __name__ == "__main__":
    unittest.main()
