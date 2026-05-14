# Collatz

In this repo, we attempt to calculate how many steps it would take for an integer n to reach 1 for sequences of integers that have to do with Collatz conjecture.

First we attempt a naïve recursive solution to the problem. After which we try a top-down memoization approach.
We then try to compare their performance in terms of how much time it takes to calculate the required steps for increasing n.

More on Collatz conjecture here: https://en.wikipedia.org/wiki/Collatz_conjecture

## How to get going

1) Create a virtual environment and activate it (unix / linux)
```bash
python -m venv venv && source venv/bin/activate
```

2) Ensure u have the latest version of pip
```bash
pip install --upgrade pip
```

3) Install requirements
```bash
pip install -r requirements.txt
```

4) Run the script
```bash
python Collatz
```