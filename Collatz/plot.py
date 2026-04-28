import matplotlib.pyplot as plt 

def plot(recursive: list, top_down: list):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(1, len(recursive) + 1), recursive, label="time recursive")
    ax2.plot(range(1, len(top_down) + 1), top_down, label="time top down")

    plt.show()