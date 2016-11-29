import pymc as pm
import numpy as np
import matplotlib.pyplot as plt
# This file illustrates various ways to calculate auto-correlation of a vector.
# Method (i): Use numpy to create, and then correlate a vector.

d = [1,2,3,1,2] # mean = 3
t = np.array(d,dtype="float")
auto = np.correlate(t,t,"full")
#print auto[auto.size/2:] # Gives us the right correlation for t>0. 


# Method (ii): 

def autocorr(x,t):
    return np.corrcoef(np.array([x[0:len(x)-t],x[t:len(x)]]))
#print autocorr([1,2,3,1,2],1)


# Method (iii): 
def autocorr1(x,t):
    lag=len(x)-1
   
    return lag
print autocorr1([1,2,3,1,2],0)

