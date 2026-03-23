"""Bubble Sort learning scaffold.

This file is intentionally incomplete. You will implement each TODO step-by-step.
Run this file often as you fill stubs in.
"""

from typing import List, Optional


def parse_numbers(raw_text: str) -> List[int]:
    """Convert user input like "5, 2, 9, 1" into a list of ints.

    TODO:
    1. Split raw_text by comma.
    2. Strip whitespace for each chunk.
    3. Convert each chunk into int.
    4. Return the list.

    Hint:
    - Start with a basic for-loop; avoid one-liners until it is clear.
    """
    # 1. Split raw_text by comma.
    chunks = raw_text.split(",")
    numbers = []

    for chunk in chunks:
        # 2. Strip whitespace for each chunk.
        clean_chunk = chunk.strip()

        # 3. Convert each chunk into int (ignoring empty strings from trailing commas).
        if clean_chunk:
            numbers.append(int(clean_chunk))

    # 4. Return the list.
    return numbers


def bubble_sort_step(numbers: List[int], last_unsorted_index: int) -> bool:
    """Run one Bubble Sort pass from index 0 up to last_unsorted_index.

    Returns:
    - True if at least one swap happened in this pass.
    - False if no swaps happened.

    TODO:
    1. Track whether any swap happened (swapped = False).
    2. Loop i from 0 to last_unsorted_index - 1.
    3. Compare numbers[i] and numbers[i + 1].
    4. If out of order, swap them and set swapped = True.
    5. Return swapped.
    """
    # 1. Track whether any swap happened.
    swapped = False

    # 2. Loop i from 0 to last_unsorted_index - 1.
    # We stop at last_unsorted_index - 1 so numbers[i+1] doesn't go out of bounds.
    for i in range(last_unsorted_index):
        # 3. Compare numbers[i] and numbers[i + 1].
        if numbers[i] > numbers[i + 1]:
            # 4. If out of order, swap them and set swapped = True.
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True

    # 5. Return swapped.
    return swapped


def bubble_sort(numbers: List[int]) -> List[int]:
    """Sort numbers in ascending order using Bubble Sort.

    TODO:
    1. Decide if you want to sort in place or on a copy.
       - Learning suggestion: work on a copy to avoid side effects.
    2. Run repeated passes from right to left boundary.
    3. Add early-stop optimization:
       - If a pass makes no swaps, break early.
    4. Return the sorted list.

    Think:
    - Why can the right boundary shrink after each pass?
    """
    # 1. Work on a copy to avoid modifying the original list passed in.
    arr = list(numbers)
    n = len(arr)

    # 2. Run repeated passes. After each pass, the largest remaining
    # element "bubbles up" to the end, so we can shrink the boundary.
    for pass_num in range(n - 1, 0, -1):
        # 3. Add early-stop optimization.
        did_swap = bubble_sort_step(arr, pass_num)

        if not did_swap:
            # If no elements were swapped, the list is already sorted!
            break

    # 4. Return the sorted list.
    return arr


def get_user_numbers() -> Optional[List[int]]:
    """Ask user for input and parse it safely.

    TODO:
    1. Prompt user for comma-separated integers.
    2. Call parse_numbers.
    3. Handle ValueError and print a helpful message.
    4. Return None on invalid input.
    """
    # 1. Prompt user.
    user_input = input("Enter numbers separated by commas (e.g., 5, 2, 9, 1): ")

    try:
        # 2. Call parse_numbers.
        return parse_numbers(user_input)
    except ValueError:
        # 3. Handle ValueError.
        print(
            "Error: That didn't look like a list of integers. Try again with numbers and commas."
        )
        # 4. Return None on invalid input.
        return None


def main() -> None:
    """Program entry point.

    TODO:
    1. Call get_user_numbers.
    2. If result is None, stop early.
    3. Call bubble_sort.
    4. Print both original and sorted list.

    Extra challenge:
    - Print the list after each pass to visualize Bubble Sort.
    """
    # 1. Call get_user_numbers.
    original_list = get_user_numbers()

    # 2. If result is None, stop early.
    if original_list is None:
        return

    # 3. Call bubble_sort.
    sorted_list = bubble_sort(original_list)

    # 4. Print results.
    print(f"\nOriginal list: {original_list}")
    print(f"Sorted list:   {sorted_list}")


if __name__ == "__main__":
    main()
