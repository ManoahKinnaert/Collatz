import sys 
import os 
from datetime import datetime

from plot import plot 

# set max recursion depth
sys.setrecursionlimit(10000)

def f(n: int):
    if not n % 2: return n // 2
    else: return 3 * n + 1

def collatz_recursive(i: int, n: int):
    if i == 0: return n
    elif i > 0: return f(collatz_recursive(i - 1, n))
    else: print("Invalid")


def run_collatz_recursive(n: int):
    i = 0
    while True:
        num = collatz_recursive(i, n)
        i += 1
        if num == 1: break 
    return i - 1

def determine_collatz_recursive(max_n: int):
    N = range(1, max_n + 1)
    steps = []
    for n in N:
        step = run_collatz_recursive(n)
        steps.append(step)

    print("[DEBUG]: Steps in function of n:", steps)
    print("[DEBUG]: Max N =", len(steps))
    return steps 

def run_collatz_exp_recursive(max_n: int):
    times = []
    for n in range(1, max_n + 1):
        t1 = datetime.now()
        determine_collatz_recursive(n)
        t2 = datetime.now()
        delta_t = t2 - t1 
        times.append(delta_t.total_seconds() * 1000)
    return times 

if __name__ == "__main__":
    max_n = os.getenv("N")
    if max_n is None: max_n = 100
    times = run_collatz_exp_recursive(max_n)
    print("Time required per n in milliseconds:", times)
    plot(times)