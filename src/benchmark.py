import time
from pathlib import Path
from matplotlib import pyplot as plt

from parse_input import parse_input
from hvlcs import compute_hvlcs
from backtrack import backtrack_sequence


def question_one():
    input_dir = Path(__file__).resolve().parent.parent / "input"
    test_files = input_dir.glob("test*.txt")

    runtimes = []
    labels = []

    for test_file in test_files:
        values, a, b = parse_input(str(test_file))

        start = time.perf_counter()
        dp = compute_hvlcs(a, b, values)
        backtrack_sequence(dp, a, b, values)
        elapsed_ms = (time.perf_counter() - start) * 1000

        runtimes.append(elapsed_ms)
        labels.append(test_file.name)

        print(f"{test_file.name}: {elapsed_ms:.4f} ms")

    # Plot the runtimes
    plt.figure(figsize=(10, 6))
    plt.bar(labels, runtimes, color='blue')
    plt.xlabel('Test Files')
    plt.ylabel('Runtime (ms)')
    plt.title('Runtime Comparison for HVLCs Computation')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    question_one()
