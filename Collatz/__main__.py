def f(n :int):
    if not n % 2: return n // 2
    else: return 3 * n + 1

def collatz_recursive(i: int, n: int):
    if i == 0: return n 
    elif i > 0: return f(collatz_recursive(i - 1, n))

def count_recursive_steps():
    pass  

def main():
    pass 

if __name__ == "__main__":
    pass 