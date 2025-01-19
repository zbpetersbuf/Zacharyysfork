
#imported libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv
import numpy as np

#opening the csv file and giving variables to the data
with open('NMR.csv', 'r') as file:
    content = csv.reader(file)

    time = []
    amp = []

    for row in content:
        time.append(row[0])
        amp.append(row[1])

#plotting the data in the csv file
plt.plot(time,amp)
plt.xlabel('time (ms)')
plt.ylabel('Pulse Amplitude (V)')
plt.title('NMR Data Analysis')

#inverting the y-axis
plt.gca().invert_yaxis()

#saving the figure
plt.savefig('NMR_plot.png', dpi = 300)

plt.show()
