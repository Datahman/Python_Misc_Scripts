import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(0,1,200)
x[0]=0
y = np.arange(0,200,1)

x_t = np.zeros(200)
for i in range(1,200):
    x_t[i] = np.random.normal(x_t[i-1],1)

    
fig=plt.figure()
ax=fig.add_subplot(211)
ax.plot(y,x,label="$x'_{t}$")

ax.plot(y,x_t,label="$x_{t}$")
ax.legend()
ax.set_title("Illustration of random distributed data points at time")
ax.set_xlabel("$t$")
ax.set_ylabel(" $x(t)$")


def autocorr(d):
    result = np.correlate(d,d,mode="full")
    result = result / np.max(result) # Divide by max of result to normalize.
    result = result[result.size/2:] # Divide by "2" to only consider t>0 vals.
    #result = np.max(result) # 4.5e4
    return result

colors = ["#348ABD", "#A60628", "#7A68A6"]
ax1 = fig.add_subplot(212)
p = np.arange(1, 200)
ax1.bar(p, autocorr(x)[1:], width=1, label="$x_t$",
        edgecolor=colors[0], color=colors[0])
ax1.bar(p, autocorr(x_t)[1:], width=1, label="$x'_t$",
        color=colors[1], edgecolor=colors[1])

ax1.legend(title="Autocorrelation")
ax1.set_ylabel("measured correlation \nbetween $x_t$ and $x_{t-k}$.")
ax1.set_xlabel("k (lag)")
ax1.set_title("Autocorrelation plot of $x'_t$ and $x_t$ for differing $t$ lags.");
plt.show()

#print(autocorr(x_t))
# Note x't series shows maxmium correlation at t=0, and decaying afterwards, whereas no correlation for x't.