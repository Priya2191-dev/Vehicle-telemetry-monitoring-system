import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def plot_data(speed, pressure):
    plt.plot(speed)
    plt.plot(pressure)
    plt.savefig("plot.png")
    plt.close()
