import matplotlib.pyplot as plt
from dateutil.parser import parse
import numpy as np

def plot(x, y, S):

    x = [parse(i) for i in x]
    x_plot = [i for i in range(1, 2*len(x), 2)]
    # print x, y

    x_plot = x_plot[:15]
    y_plot = np.array(y[:15])
    y_plot = (y_plot - np.mean(y_plot)) + 1

    plt.bar(x_plot, y_plot, color='red', alpha=0.75)
    val = 0
    for i, j in zip(x_plot, y_plot):
        plt.annotate(str(S[val]), xy=(i, j+0.005))
        val += 1
    plt.title('Stock span problem (Mean Square Difference)')
    plt.show()
