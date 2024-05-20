# !/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# parameters to modify
filename="processed_iperf_test3.txt"
label1='iperf1 s to c'
label2='iperf2 c to s'
xlabel = 'interval'
ylabel = 'Bandwidth in Mbits/s'
title='RP as server LM as client bi-directional t=10 i=1'
fig_name='iperf_3_graph'
bins=5000 #adjust the number of bins to your plot


t = np.loadtxt(filename, delimiter=" ", dtype="float")

i=t[:,0]
l=t[:,1]

plt.plot(i[::2], l[::2], label=label1)# Plot some data on the (implicit) axes.
plt.plot(i[::2], l[1::2], label=label2)
#Comment the line above and uncomment the line below to plot a CDF
#plt.hist(t[:,1], bins, density=True, histtype='step', cumulative=True, label=label)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()
plt.savefig(fig_name)
plt.show()
