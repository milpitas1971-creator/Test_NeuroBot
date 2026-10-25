"""Unit tests for employee_database.py."""

import contextlib
import io
import os
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

import employee_database


class EmployeeDatabaseTests(unittest.TestCase):
    def test_prompt_required_retries_empty_input(self):
        with (
            patch("builtins.input", side_effect=["  ", "Rudy"]),
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            value = employee_database.prompt_required("Employee name")

        self.assertEqual(value, "Rudy")
        self.assertIn("cannot be empty", output.getvalue())

    def test_prompt_experience_retries_invalid_negative_and_infinite_values(self):
        with (
            patch("builtins.input", side_effect=["unknown", "-1", "inf", "2.5"]),
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            value = employee_database.prompt_experience()

        self.assertEqual(value, 2.5)
        self.assertIn("Please enter a valid number", output.getvalue())
        self.assertIn("must be a non-negative number", output.getvalue())

    def test_main_creates_database_and_saves_employee(self):
        with tempfile.TemporaryDirectory() as directory:
            original_directory = os.getcwd()
            try:
                os.chdir(directory)
                with (
                    patch("builtins.input", side_effect=["Rudy", "Engineer", "2.5"]),
                    contextlib.redirect_stdout(io.StringIO()) as output,
                ):
                    employee_database.main()

                connection = sqlite3.connect("employees.db")
                try:
                    row = connection.execute(
                        """
                        SELECT employee_name, position, years_of_experience
                        FROM employees
                        """
                    ).fetchone()
                finally:
                    connection.close()
            finally:
                os.chdir(original_directory)

        self.assertEqual(row, ("Rudy", "Engineer", 2.5))
        self.assertIn("Employee details saved to employees.db.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
