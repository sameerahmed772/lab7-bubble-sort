import pytest

from main import bubble_sort, bubble_sort_step, get_user_numbers, parse_numbers


def test_parse_numbers_valid_and_current_lenient_behavior():
    assert parse_numbers(" 10, -3, 0, ") == [10, -3, 0]


def test_parse_numbers_raises_on_non_integer_token():
    with pytest.raises(ValueError):
        parse_numbers("1, two, 3")


def test_bubble_sort_step_swaps_and_reports_true():
    values = [5, 1, 3]

    did_swap = bubble_sort_step(values, 2)

    assert did_swap is True
    assert values == [1, 3, 5]


def test_bubble_sort_returns_sorted_copy_without_mutating_input():
    original = [4, 2, 2, 9, -1]

    result = bubble_sort(original)

    assert result == [-1, 2, 2, 4, 9]
    assert original == [4, 2, 2, 9, -1]


def test_get_user_numbers_handles_invalid_input(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "1, hello, 3")

    result = get_user_numbers()
    output = capsys.readouterr().out

    assert result is None
    assert "didn't look like a list of integers" in output
