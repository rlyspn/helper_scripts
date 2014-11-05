from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import operator


def get_cdf_points(values):
    x = []
    y = []

    val_counter = Counter(values)

    total_values = float(len(values))
    current_prop = 0.0
    for val, count in sorted(val_counter.iteritems(),
                             key=operator.itemgetter(0)):
        fraction = count / total_values
        current_prop += fraction
        x.append(val)
        y.append(current_prop)

    if x[0] > 0:
        x = [x[0]] + x
        y = [0] + y
    return x, y


def set_labels(xaxis, yaxis, title):
    font_size = 24
    if xaxis is not None:
        plt.xlabel(xaxis, fontsize=font_size)
    if yaxis is not None:
        plt.ylabel(yaxis, fontsize=font_size)
    if title is not None:
        plt.title(title, fontsize=font_size)


def plot_points(x, y, xaxis=None, yaxis=None, title=None):
    set_labels(xaxis, yaxis, title)
    plt.plot(x, y, linewidth=5)
    plt.show()


def plot_bar_chart(values, ticks=None, xaxis=None, yaxis=None, title=None):
    width = 0.75
    n = len(values)
    set_labels(xaxis, yaxis, title)
    if ticks is not None:
        plt.xticks(np.arange(n) + width / 2, ticks, rotation=50,
                   fontsize=18)
    plt.bar(np.arange(n), values, width)
    plt.show()
