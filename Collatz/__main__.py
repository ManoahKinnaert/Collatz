def f(n: int):
    if not n % 2: return n // 2
    else: return 3 * n + 1

def collatz_recursive(i: int, n: int):
    if i == 0: return n
    elif i > 0: return f(collatz_recursive(i - 1, n))
    else: print("Invalid")


if __name__ == "__main__":
    import os
    n = int(os.getenv("N"))
    print(n)
    i = 0
    while True:
        num = collatz_recursive(i, 12)
        i += 1
        print(num)
        if num == 1: break 
    print("Num of steps:", i - 1)