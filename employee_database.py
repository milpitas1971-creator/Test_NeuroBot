"""Collect employee details and save them in a local SQLite database."""

import math
import sqlite3


def prompt_required(label):
    """Prompt until a non-empty value is entered."""
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print(f"{label} cannot be empty.")


def prompt_experience():
    """Prompt for a non-negative number of years of experience."""
    while True:
        value = input("Years of experience: ").strip()
        try:
            years = float(value)
        except ValueError:
            print("Please enter a valid number of years.")
            continue
        if math.isfinite(years) and years >= 0:
            return years
        print("Years of experience must be a non-negative number.")


def main():
    employee_name = prompt_required("Employee name")
    position = prompt_required("Position")
    years_of_experience = prompt_experience()

    connection = sqlite3.connect("employees.db")
    try:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_name TEXT NOT NULL,
                    position TEXT NOT NULL,
                    years_of_experience REAL NOT NULL
                )
                """
            )
            connection.execute(
                """
                INSERT INTO employees (employee_name, position, years_of_experience)
                VALUES (?, ?, ?)
                """,
                (employee_name, position, years_of_experience),
            )
    finally:
        connection.close()

    print("Employee details saved to employees.db.")


if __name__ == "__main__":
    main()
