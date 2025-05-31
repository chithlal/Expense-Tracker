# Expense Tracker

A simple command-line Expense Tracker written in Python. It allows you to add, view, and save expenses, as well as set and track your budget. Expenses are stored in a CSV file.

## Features

- Add new expenses with amount, category, and description
- View all recorded expenses
- Set a budget and track remaining budget
- Save expenses to a CSV file (`expenses.csv`)
- Loads existing expenses from CSV on startup

## Getting Started

### Prerequisites

- Python 3.x

### Usage

1. Clone or download this repository.
2. Make sure `ExpenseTracker.py` and `expenses.csv` are in the same directory.
3. Run the program:

```sh
python ExpenseTracker.py
```

4. Follow the on-screen menu to add expenses, view expenses, set a budget, and save your data.

### File Structure

- `ExpenseTracker.py` - Main Python script containing the application logic.
- `expenses.csv` - CSV file where expenses are stored.
- `expenses.txt` - Example or alternative expenses file.
- `ExpenseTracker-src.txt` - Source code backup or reference.

### Example CSV Format

```
amount,category,description
100.0,food,hotel
200.0,study,AI
```

## License

This project is for educational purposes.
