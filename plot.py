import matplotlib.pyplot as plt
import numpy as np


def plot_graph(data, ylim=[-1.5, 1.5], text=[]):
    bit_duration = 1
    padding = 0.5

    time = np.arange(0, len(data) * bit_duration + 1, 0.01)

    signal = []
    t_axis = []
    for i, bit in enumerate(data):
        t_axis.extend([i * bit_duration, (i + 1) * bit_duration])
        signal.extend([bit, bit])

    plt.figure(figsize=(8, 4))
    plt.plot(t_axis, signal, color='magenta', linewidth=4)

    for i, bit in enumerate(text):
        plt.text(i * bit_duration + 0.5, 1.2, str(bit), fontsize=12, color='magenta', ha='center')

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xticks(np.arange(0, len(data) + 1, 1))
    plt.yticks([0, 1], ['0', 'V'])
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    plt.grid(axis='x', linestyle='--')

    plt.xlim(-padding, len(data) * bit_duration + padding)
    plt.ylim(ylim[0], ylim[1])

    plt.show()


if __name__ == '__main__':
    data = [1, 0, -1, 0, 0, 1, 1, -1]
    plot_graph(data)