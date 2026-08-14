# CSV Expense Tracker

A CLI of an Expense Tracker app that helps you track your expenses and saves
it in a csv file.

## Features
- Lets you add, view, and get summary of  the total expenses and for each category of
expenses.
- Lets file content persist across sessions by saving it in `expense tracker.csv`.
- Handles first time properly when file doesn't exist yet.
- Auto adds a date for each expense
- Handles invalid `Amount` and `Category` inputs without crashing.

## How it works
- `load_file()` uses `try/except` to handle the case where the file doesn't exist yet. If it doesn't, 
it creates the file in "w" mode and writes the headers.
- `add_expense()` opens the file in "a" mode to add an expense to the file without risking the
rest of its content.
- `Category` accepts only `Purchase` and `Personal` inputs to keep it more organized and easier
to summarize.
- Validated `Amount` by wrapping `float(first)` inside `try/except` to handle Value Errors that may arise
from invalid inputs. 

## What I Learned
- I struggled with getting the total of both categories and then improved my knowledge on how to build a dictionary from a dictionary or list and was able to arrive at `category_totals[row["Category"]] = category_totals.get(row["Category"], 0 ) + float(row["Amount"])` in `summary()`
- Still in `summary()`, I ran two separate loops for the total expense and the category totals. One ran and the other didn't, this meant a loop(iterator) can only be ran once. So I corrected and placed the totals in one loop. 


## How to Run It
```bash
python csv_expense_tracker.py
```


## Possible Improvements
- Could use both a date and a time stamp instead of just a date.
- Editing previously entered entries.