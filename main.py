"""Bubble Sort CLI with optional in-place terminal animation.

This module provides:
- input parsing for comma-separated integers
- standard Bubble Sort
- animated Bubble Sort with in-place ASCII redraw
"""

import sys
import time
from typing import List, Optional


def parse_numbers(raw_text: str) -> List[int]:
    """Convert comma-separated text into a list of integers.

    Empty chunks are ignored, so input like "1,,2," becomes [1, 2].
    """
    chunks = raw_text.split(",")
    numbers = []

    for chunk in chunks:
        clean_chunk = chunk.strip()
        # Ignoring empty chunks allows inputs like "1,,2" or trailing commas to still work
        if clean_chunk:
            numbers.append(int(clean_chunk))

    return numbers


def bubble_sort_step(numbers: List[int], last_unsorted_index: int) -> bool:
    """Run one Bubble Sort pass and return whether any swap occurred."""
    swapped = False

    for i in range(last_unsorted_index):
        if numbers[i] > numbers[i + 1]:
            # Swap the elements
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True

    return swapped


def bubble_sort(numbers: List[int]) -> List[int]:
    """Return a sorted copy of numbers using Bubble Sort."""
    arr = list(numbers)
    n = len(arr)

    for pass_num in range(n - 1, 0, -1):
        did_swap = bubble_sort_step(arr, pass_num)

        if not did_swap:
            break

    return arr


def format_bars_frame(
    numbers: List[int],
    sorted_from: int,
    active_left: Optional[int] = None,
) -> str:
    """Build a single ASCII frame for the current sorting state.

    - Items in the sorted suffix are labeled as sorted.
    - The active comparison pair is highlighted.
    """
    lines = []

    for i, val in enumerate(numbers):
        # Handle negative numbers visually with a different character if needed
        bar_char = "#" if val >= 0 else "!"
        bar = bar_char * abs(val)

        label = ""
        if active_left is not None and (i == active_left or i == active_left + 1):
            label = " <-- COMPARING"
        elif i >= sorted_from:
            label = " (Sorted)"

        # Format the number to keep the bars aligned
        lines.append(f"{val:3} | {bar}{label}")

    return "\n".join(lines)


def redraw_in_place(frame_text: str, previous_lines: int) -> int:
    """Redraw a multi-line frame in-place and return its line count."""
    # 1. Move cursor up
    if previous_lines > 0:
        sys.stdout.write(f"\033[{previous_lines}F")

    # 2 & 3. Clear line and print new frame
    for line in frame_text.split("\n"):
        sys.stdout.write("\033[2K")  # ANSI escape to clear the entire line
        sys.stdout.write(line + "\n")

    # 4. Flush to ensure smooth animation
    sys.stdout.flush()

    # 5. Return new line count
    return len(frame_text.split("\n"))


def bubble_sort_animated(numbers: List[int], delay_seconds: float = 0.20) -> List[int]:
    """Return a sorted copy while rendering in-place comparison frames."""
    arr = list(numbers)
    n = len(arr)
    lines_used = 0

    print("\nStarting Animation...")

    for pass_num in range(n - 1, 0, -1):
        swapped_in_pass = False

        for i in range(pass_num):
            # Render comparison frame
            frame = format_bars_frame(arr, pass_num + 1, active_left=i)
            lines_used = redraw_in_place(frame, lines_used)
            time.sleep(delay_seconds)

            # Check and swap
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped_in_pass = True

                # Render swap frame
                frame = format_bars_frame(arr, pass_num + 1, active_left=i)
                lines_used = redraw_in_place(frame, lines_used)
                time.sleep(delay_seconds)

        # Early stop optimization
        if not swapped_in_pass:
            break

    # Final done frame
    final_frame = format_bars_frame(arr, 0)
    redraw_in_place(final_frame, lines_used)
    print("\nSorting Complete!")

    return arr


def get_user_numbers() -> Optional[List[int]]:
    """Prompt user for comma-separated numbers and parse safely."""
    raw_text = input("Enter numbers separated by commas (e.g., 5, 2, 9, 1): ")

    try:
        return parse_numbers(raw_text)
    except ValueError:
        print("Error: That didn't look like a list of integers. Try again with numbers and commas.")
        return None


def ask_use_animation() -> bool:
    """Ask whether to run animated sorting mode."""
    choice = input("Would you like to run the animated mode? (y/n): ").strip().lower()
    return choice in {"y", "yes"}


def main() -> None:
    """Run the Bubble Sort CLI flow."""
    original_list = get_user_numbers()

    if original_list is None:
        return

    use_animation = ask_use_animation()

    if use_animation:
        sorted_list = bubble_sort_animated(original_list)
    else:
        sorted_list = bubble_sort(original_list)

    print(f"\nOriginal list: {original_list}")
    print(f"Sorted list:   {sorted_list}")


if __name__ == "__main__":
    main()
