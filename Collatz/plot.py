import matplotlib.pyplot as plt 

def plot(recursive: list):
    fig, ax = plt.subplots(1, 1)
    ax.plot(range(1, len(recursive) + 1), recursive)

    plt.show()