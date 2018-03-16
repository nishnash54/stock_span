from data import return_data
from plot import plot

def calculateSpan(price, n, S):

    S[0] = 1
    for i in range(1, n, 1):
        S[i] = 1
        j = i - 1
        while (j>=0) and (price[i] >= price[j]) :
            S[i] += 1
            j -= 1

if __name__ == "__main__":

    sym = "MSFT"
    x_data, y_data = return_data(sym)
    num = len(y_data)
    S = [None] * num
    calculateSpan(y_data, num, S)
    print S
    plot(x_data, y_data, S)
