from dynamic_solutions import measure_perf_top_down
from recursive_solutions import measure_perf_recursive
from plot import plot_results

def main():
    max_n = 1000000
    top_down = measure_perf_top_down(max_n)
    recursive = measure_perf_recursive(max_n)
    plot_results(range(1, max_n + 1), top_down, recursive)

if __name__ == "__main__":
    main() 