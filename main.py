"""Bubble Sort learning scaffold for terminal in-place redraw.

This version is intentionally incomplete.
Implement each TODO in order and run often while you build it.
"""

import sys
import time
from typing import List, Optional


def parse_numbers(raw_text: str) -> List[int]:
    """Convert user input like "5, 2, 9, 1" into a list of ints.

    TODO:
    1. Split by comma.
    2. Strip whitespace from each item.
    3. Convert each item to int.
    4. Return the list.

    Think:
    - Should empty chunks like "1,,2" be accepted or rejected?
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
    """Run one Bubble Sort pass from index 0 to last_unsorted_index.

    Returns True if at least one swap happened in this pass.

    TODO:
    1. Track a swapped flag.
    2. Compare adjacent pairs up to last_unsorted_index.
    3. Swap out-of-order values.
    4. Return whether any swap occurred.
    """
    swapped = False

    for i in range(last_unsorted_index):
        if numbers[i] > numbers[i + 1]:
            # Swap the elements
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True

    return swapped


def bubble_sort(numbers: List[int]) -> List[int]:
    """Sort values in ascending order (non-animated path).

    TODO:
    1. Work on a copy (to avoid mutating the caller's list).
    2. Run Bubble Sort passes right-to-left boundary.
    3. Use early-stop optimization if a pass has no swaps.
    4. Return sorted copy.
    """
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
    """Build one ASCII frame for the current sorting state.

    Args:
    - numbers: current list state
    - sorted_from: first index of sorted suffix
    - active_left: left index of active comparison pair

    TODO:
    1. Render one line per value.
    2. Draw ASCII bars for values.
    3. Mark sorted suffix values differently.
    4. Mark active comparison pair (active_left and active_left + 1).
    5. Return full multi-line frame string.
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
    """Redraw frame in-place using ANSI escape sequences.

    Args:
    - frame_text: multi-line frame to print
    - previous_lines: number of lines printed by previous frame

    Returns:
    - number of lines printed for this frame

    TODO:
    1. If previous_lines > 0, move cursor up by that many lines.
    2. Clear each line before writing new content.
    3. Print the new frame.
    4. Flush stdout so animation appears immediately.
    5. Return current frame line count.

    Hint:
    - Useful ANSI sequences include cursor-up and clear-line.
    """
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
    """Sort with Bubble Sort while rendering frames in-place.

    TODO:
    1. Work on a copy of numbers.
    2. Track how many lines were used by the previous frame.
    3. For each pass, render comparison frames (and swap frames if desired).
    4. Sleep delay_seconds between frames.
    5. Keep early-stop optimization.
    6. Draw a final "done" frame and return sorted copy.

    Note:
    - Import time and sys only when you implement this function.
    """
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
    """Prompt user and parse input safely.

    TODO:
    1. Read input string.
    2. Call parse_numbers.
    3. Handle ValueError with a helpful message.
    4. Return None on invalid input.
    """
    raw_text = input("Enter numbers separated by commas (e.g., 5, 2, 9, 1): ")

    try:
        return parse_numbers(raw_text)
    except ValueError:
        print(
            "Error: Input contains invalid characters. Please enter only integers and commas."
        )
        return None


def ask_use_animation() -> bool:
    """Ask whether to run animated sorting mode.

    TODO:
    1. Prompt user with y/n question.
    2. Normalize input (trim/lowercase).
    3. Return True for yes, False for no.
    """
    choice = input("Would you like to run the animated mode? (y/n): ").strip().lower()
    return choice == "y" or choice == "yes"


def main() -> None:
    """Program entry point.

    TODO:
    1. Read numbers with get_user_numbers.
    2. Exit early when input is invalid.
    3. Ask for mode with ask_use_animation.
    4. Call bubble_sort or bubble_sort_animated.
    5. Print original and sorted results.
    """
    original_list = get_user_numbers()

    if original_list is None:1
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
