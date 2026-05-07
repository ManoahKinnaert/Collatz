import matplotlib.pyplot as plt 

def plot_results(x: list, iterative: list, recursive: list):
    plt.style.use("ggplot")

    fig, ax = plt.subplots(1, 1)
    ax.plot(x, recursive, label="Recursive")
    ax.plot(x, iterative, label="Iterative")
    ax.set_title("Collatz")
    ax.set_xlabel("N")
    ax.set_ylabel("Required time")
    ax.legend()

    plt.show()