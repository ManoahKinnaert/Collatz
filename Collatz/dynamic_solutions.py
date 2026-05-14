from tqdm import trange
import time 

def f(n: int):
    if not n % 2: return n // 2
    else: return 3 * n + 1

def top_down(n: int, memo: dict={1: 0}):
    if n in memo:
        return memo[n]

    steps = 1 + top_down(f(n), memo)
    memo[n] = steps
    return steps 

def iterative(n: int):
    steps = 0
    while True:
        if n == 1: break
        n = f(n)
        steps += 1
    return steps

def measure_perf_top_down(max_n: int):
    times = []
    for n in trange(1, max_n + 1):
        start = time.perf_counter()
        top_down(n)
        end = time.perf_counter()
        times.append(end - start)
    return times 

def measure_perf_iterative(max_n: int):
    times = []
    for n in trange(1, max_n + 1):
        start = time.perf_counter()
        iterative(n)
        end = time.perf_counter()
        times.append(end - start)
    return times  

if __name__ == "__main__":
    print(measure_perf_top_down(12))
    print(iterative(12))