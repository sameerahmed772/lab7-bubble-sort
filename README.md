# Lab 7: Bubble Sort Application

This repository contains a Bubble Sort command-line app in Python with two modes:
- standard sorting output
- animated in-place terminal visualization

## What This Project Covers

- Parsing comma-separated user input into integers
- Running Bubble Sort one pass at a time
- Full Bubble Sort with early-stop optimization
- In-place ASCII visualization in the terminal using ANSI redraw
- Defensive input handling for invalid values
- Basic automated testing with pytest

## Requirements

- Python 3.10+ (project currently runs on Python 3.14)

## Run the App

From the project root:

```bash
python3 main.py
```

If you want to use the exact interpreter configured in this workspace:

```bash
/opt/homebrew/bin/python3 main.py
```

If you are using the local virtual environment:

```bash
.venv/bin/python main.py
```

Example interaction (standard mode):

```text
Enter numbers separated by commas (e.g., 5, 2, 9, 1): 10, 5, 8, 1, 7

Original list: [10, 5, 8, 1, 7]
Sorted list:   [1, 5, 7, 8, 10]
```

Example interaction (animated mode):

```text
Enter numbers separated by commas (e.g., 5, 2, 9, 1): 10, 5, 8, 1, 7
Would you like to run the animated mode? (y/n): y

Starting Animation...
...in-place bar redraw frames...
Sorting Complete!

Original list: [10, 5, 8, 1, 7]
Sorted list:   [1, 5, 7, 8, 10]
```

Note:
- In-place redraw works best in ANSI-capable interactive terminals.
- If a terminal does not support ANSI cursor movement, output may look less clean.

## Testing

Run tests with:

```bash
.venv/bin/python -m pytest -q
```

Current test suite includes 5 tests in `tests/test_main.py`.

## Project Structure

- `main.py`: Bubble Sort app, CLI flow, and animation helpers
- `tests/test_main.py`: pytest test cases
- `pytest.ini`: pytest discovery configuration
- `REPORT.md`: project report
- `JOURNAL.md`: interaction and change log

## Notes for Learners

- Start by understanding `parse_numbers`, then `bubble_sort_step`, then `bubble_sort`.
- Test edge cases like empty input, repeated values, negatives, and invalid tokens.
- Improve robustness by deciding whether malformed input (like `1,,2`) should be rejected or accepted.