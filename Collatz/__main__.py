from dynamic_solutions import measure_perf_top_down, measure_perf_iterative
from recursive_solutions import measure_perf_recursive
from plot import plot_results_top_vs_recursive, plot_results_top_vs_iter

def main():
    max_n = 1000000
    x = range(1, max_n + 1)
    top_down = measure_perf_top_down(max_n)
    recursive = measure_perf_recursive(max_n)
    iterative = measure_perf_iterative(max_n)
    #plot_results_top_vs_recursive(x, top_down, recursive)
    plot_results_top_vs_iter(x, top_down, iterative)

if __name__ == "__main__":
    main() 