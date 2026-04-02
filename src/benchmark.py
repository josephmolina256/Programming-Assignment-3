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
    figure, axis = plt.subplots(figsize=(10, 6))
    axis.bar(labels, runtimes, color="blue")
    axis.set_xlabel("Test Files")
    axis.set_ylabel("Runtime (ms)")
    axis.set_title("Runtime Comparison for HVLCS Computation")
    axis.tick_params(axis="x", rotation=45)
    figure.tight_layout()

    output_dir = Path(__file__).resolve().parent.parent / "output"
    output_dir.mkdir(exist_ok=True)
    figure.savefig(output_dir / "Figure_1.png", dpi=200)
    plt.close(figure)



if __name__ == "__main__":
    question_one()
