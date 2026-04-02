import time
from pathlib import Path

from parse_input import parse_input
from hvlcs import compute_hvlcs
from backtrack import backtrack_sequence


def question_one():
    input_dir = Path(__file__).resolve().parent.parent / "input"
    test_files = sorted(input_dir.glob("test*.txt"))

    for test_file in test_files:
        values, a, b = parse_input(str(test_file))

        start = time.perf_counter()
        dp = compute_hvlcs(a, b, values)
        backtrack_sequence(dp, a, b, values)
        elapsed_ms = (time.perf_counter() - start) * 1000

        print(f"{test_file.name}: {elapsed_ms:.4f} ms")


if __name__ == "__main__":
    question_one()
