# Bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## About

"Book Bot" - a Python program that can analyze an entire book (or any other text document) and print out an interesting statistical report. 

A few of the learning goals are:
- Configure a professional Python development environment on your local computer
- Deploy a Python project on your personal GitHub account
- Learn how to use a professional code editor (VS Code)
- Put your Python and Git skills to the test in a real project
- Refactoring

## Guided projects

Guided projects are designed to get you *out* of tutorial hell, by writing a ton of code and giving you challenges to solve on your own (you are given a few hints, but the rest is on you and Google).

## Changes made on the original project

- Use type hints.
- Use pure functions.
- Use the `.get()` method to add characters to a dictionary in the `character_count` function.
- Changed `main.py` to only set variables and execute functions. This was done by adding two more scripts and moving functions out of `main.py`:
  - `get_and_check_data.py`
      - checks if a user gave a path to a document.
      - retrieves text from the document.
  - `report.py`
    - prints an analysis report to the terminal.
