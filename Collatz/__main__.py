import sys 

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

def run_collatz_recursive_exp(max_n: int):
    N = range(1, max_n + 1)
    steps = []
    for n in N:
        step = run_collatz_recursive(n)
        steps.append(step)

    print("Steps in function of n:", steps)

if __name__ == "__main__":
    run_collatz_recursive_exp(max_n=15)