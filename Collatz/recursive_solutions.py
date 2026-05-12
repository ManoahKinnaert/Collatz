from tqdm import trange
import time 

def collatz(n: int):
    if n == 1: return 0
    elif not n % 2: return 1 + collatz(n // 2)
    else: return 1 + collatz(3 * n + 1)

def count_steps(max_n: int):
    steps = []
    for n in trange(1, max_n + 1):
        steps.append(collatz(n))
    return steps

def measure_perf_recursive(max_n: int):
    times = []
    for n in trange(1, max_n + 1):
        start = time.perf_counter()
        collatz(n)
        end = time.perf_counter()
        times.append(end - start)
    return times 

if __name__ == "__main__":
    print(measure_perf_recursive(10000))