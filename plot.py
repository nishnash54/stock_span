import matplotlib.pyplot as plt
from dateutil.parser import parse

def plot(x, y):

    x = [parse(i) for i in x]
    x_plot = [i for i in range(1, len(x)+1)]
    print x, y

    plt.plot(x_plot, y, color='red', alpha=0.75)
    plt.title('Stock prices')
    plt.show()
