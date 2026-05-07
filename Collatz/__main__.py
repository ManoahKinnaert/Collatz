def f(n :int):
    if not n % 2: return n // 2
    else: return 3 * n + 1

def collatz_recursive(n :int):
    if n == 1: return 0
    return 1 + collatz_recursive(f(n))

def main():
    print(collatz_recursive(12))

if __name__ == "__main__":
    main() 