import matplotlib.pyplot as plt 

def plot_results_top_vs_recusive(x: list, top_down: list, recursive: list):
    plt.style.use("ggplot")

    fig, ax = plt.subplots(1, 1)
    ax.plot(x, recursive, label="Recursive")
    ax.plot(x, top_down, label="Top down")
    ax.set_title("Collatz")
    ax.set_xlabel("N")
    ax.set_ylabel("Required time")
    ax.legend()

    plt.show()

def plot_results_top_vs_iter(x: list, top_down: list, iter: list):
    plt.style.use("ggplot")

    fig, ax = plt.subplots(1, 1)
    ax.plot(x, iter, label="Iterative")
    ax.plot(x, top_down, label="Top down")
    ax.set_title("Collatz")
    ax.set_xlabel("N")
    ax.set_ylabel("Required time")
    ax.legend()

    plt.show()

def plot_results_iter_vs_recusive(x: list, iter: list, recursive: list):
    plt.style.use("ggplot")

    fig, ax = plt.subplots(1, 1)
    ax.plot(x, recursive, label="Recursive")
    ax.plot(x, iter, label="Iterative")
    ax.set_title("Collatz")
    ax.set_xlabel("N")
    ax.set_ylabel("Required time")
    ax.legend()

    plt.show()