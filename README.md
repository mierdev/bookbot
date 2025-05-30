# Book Bot

"Book Bot" - a Python program that can analyze an entire book (or any other `.txt` document) and print out an interesting statistical report. 

A few of the learning goals are:
- Configure a professional Python development environment on your local computer.
- Deploy a Python project on your personal GitHub account.
- Learn how to use a professional code editor (VS Code).
- Put your Python and Git skills to the test in a real project.
- Refactoring and cleaning up your code.

## Usage

Clone the repo:
```bash
git clone git@github.com:mierdev/bookbot.git
```

Run the program:
```bash
python3 main.py <path_to_book>
```

## "Guided" projects

Book Bot is my first [Boot.dev](https://www.boot.dev) project! "Guided" projects are designed to get you *out* of tutorial hell, by writing a ton of code and giving you challenges to solve on your own (you are given a few hints, but the rest is on you and Google).

## Changes made on the original project

- Use type hints.
- Use pure functions.
- Use the `.get()` method to add characters to a dictionary in the `character_count` function.
- Use the `.items()` method and a `lambda` function to sort the characters on value (descending).
- Check if the document at the by the user defined path exists.
- Changed `main.py` to only set variables and execute functions. This was done by adding two more scripts and moving functions out of `main.py`:
  - `get_and_check_data.py`
      - checks if a user gave a path to a document.
      - retrieves text from the document.
  - `report.py`
    - prints an analysis report to the terminal.
