from data import return_data
from plot import plot

if __name__ == "__main__":

    sym = "MSFT"

    x_data, y_data = return_data(sym)
    plot(x_data, y_data)
