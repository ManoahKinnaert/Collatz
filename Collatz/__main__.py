import time 
import sys 
from plot import plot_results
from tqdm import trange

sys.setrecursionlimit(10000)

def f(n :int):
    if not n % 2: return n // 2
    else: return 3 * n + 1

def collatz_recursive(n: int):
    if n == 1: return 0
    return 1 + collatz_recursive(f(n)) 

# a top down method
def collatz_iterative(n: int):
    i = 0
    while n != 1:
        n = f(n)
        i += 1
    return i 

def measure_collatz_recursive(n: int):
    start = time.perf_counter()
    collatz_recursive(n)
    end = time.perf_counter()
    return end - start 

def measure_collatz_iterative(n: int):
    start = time.perf_counter()
    collatz_iterative(n)
    end = time.perf_counter()
    return end - start 

def recursive_experiment(min_val: int=10000, max_val: int=100000):
    times = []
    for n in trange(min_val, max_val + 1):
        t = measure_collatz_recursive(n)
        times.append(t)
    return times 

def iterative_experiment(min_val: int=10000, max_val: int=100000):
    times = []
    for n in trange(min_val, max_val + 1):
        t = measure_collatz_iterative(n)
        times.append(t)
    return times  

def main():
    min_val = 100_000
    max_val = 110_000 
    recursive = recursive_experiment(min_val, max_val) 
    iterative = iterative_experiment(min_val, max_val)
    x = range(min_val, max_val + 1)
    plot_results(x, iterative, recursive)

if __name__ == "__main__":
    main() 