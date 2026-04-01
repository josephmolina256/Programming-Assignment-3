import sys

from parse_input import parse_input
from hvlcs import compute_hvlcs
from backtrack import backtrack_sequence


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <input_file>")
        return

    file_path = sys.argv[1]

    values, a, b = parse_input(file_path)

    # compute cache table
    cache = compute_hvlcs(a, b, values)

    # result
    max_value = cache[-1][-1]

    # reconstruct sequence
    sequence = backtrack_sequence(cache, a, b, values)

    print(max_value)
    print(sequence)


if __name__ == "__main__":
    main()