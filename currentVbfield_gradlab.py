import numpy as np
import matplotlib.pyplot as plt

#data below is current (A) and B-field (T)
A = [5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0]
T = [0.1056, 0.2125, 0.3179, 0.4265, 0.5258, 0.6058, 0.6678]

#plotting data from above
plt.plot(T,A)
plt.xlabel ('B-field (T)')
plt.ylabel ('Current (A)')
plt.title ('Current vs B-field')

#saving figure
plt.savefig('Current v B-field plot.png')

#show the plot
plt.show()
