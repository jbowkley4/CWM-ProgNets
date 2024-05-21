# !/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# parameters to modify
filename="processedIP3_1.txt"
label1='iperf3 test'
xlabel = 'test number'
ylabel = 'Bandwidth in Mbits/s'
title='RP as server iperf3 test'
fig_name='iperf3graph_1'
bins=5000 #adjust the number of bins to your plot


t = np.loadtxt(filename, delimiter=" ", dtype="float")

plt.plot(t[:,0], t[:,1], label=label1)# Plot some data on the (implicit) axes.
#Comment the line above and uncomment the line below to plot a CDF
#plt.hist(t[:,1], bins, density=True, histtype='step', cumulative=True, label=label)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()
plt.savefig(fig_name)
plt.show()
