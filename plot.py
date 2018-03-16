import matplotlib.pyplot as plt
from dateutil.parser import parse

def plot(x, y, S):

    x = [parse(i) for i in x]
    x_plot = [i for i in range(1, 2*len(x), 2)]
    print x, y

    x_plot = x_plot[:15]
    y = y[:15]

    plt.bar(x_plot, y, color='red', alpha=0.75)
    val = 0
    for i, j in zip(x_plot, y):
        plt.annotate(str(S[val]), xy=(i, j+0.25))
        val += 1
    plt.title('Stock span problem')
    plt.show()
