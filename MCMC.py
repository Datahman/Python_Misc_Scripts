# Demonstration of MCMC method on a bi- two cluster model.
import scipy.stats as stats
from IPython.core.pylabtools import figsize
import numpy as np
import pymc as pm
figsize(12.5, 4)

import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import norm
data = np.loadtxt("mixture_data.csv",delimiter=",")
plt.hist(data,bins=20,color="k",histtype="stepfilled",alpha=0.8)
plt.title("Histrogram of the dataset")
plt.ylim([0,None])
#plt.show()


# Now we will set a priori on a stochastic variable, call x_. Setting to clusters, x_0 and x_1, at p(x_1) = 1 - p(x_0) 
x_ = pm.Uniform("x_",0,1) # Uniform range.
assignment = pm.Categorical("Assignement",[x_,1-x_],size = data.shape[0])

print("prior assignment, with x_ = %.2f" % x_.value)
print(assignment.value[:10], "...") # Question to self: is x_ used for each assignement?

# We maintain the ignorance of sigma_0, sigma_1 and use precision definition.

# Precision , tau = 1/sigma^2

taus = 1.0 / pm.Uniform("stds",0,100,size=2)**2 # Size two since we model both taus as PyMC variable, same time.

# Note from the two graph peaks, that mu_0, mu_1, lie at 120, and 190 ish. 
# sigma_0,1 = 1 . 
centers = pm.Normal("centers",[120,190], [0.01,0.01],size=2) #Format : (variable name,mean,sdev,size)

# Now define functions to assign 0,1 for a given set of parameters.

@pm.deterministic
def center_i(assignment=assignment,centers=centers):
    return centers[assignment]
@pm.deterministic
def tau_i(assignment=assignment,taus=taus):
    return taus[assignment]
print("Random assignment:", assignment.value[:4],"...")

print("Center assignment:", centers.value[:4],"...")

print("Taus assignment:", taus.value[:4],"...")
# Set observation.
observations= pm.Normal("obs",center_i,tau_i,value=data,observed=True)

# Set model class.
model = pm.Model([x_,assignment,observations,taus,centers])

# Set the model into MCMC class to use mcmc algorithm.
mcmc=pm.MCMC(model) # Instantiate mcmc object
mcmc.sample(50000)

# Now the unknown parameters, centers_i, taus (precisions), and p can be found as following:
# Find their traces, path taken as a function of sample.

figsize(12.5,9)
plt.subplot(311) # (rows,cols,fig no.)
lw = 1
center_trace = mcmc.trace("centers")[:]
#print (np.shape(center_trace)) # shape [5000,2]
# Define coloring schemes.
 # If last value of k=1 array is larger than k=1, the following color.
if center_trace[-1,0] > center_trace[-1,1]:
    colors = ["#003865","#FF0000"]
else:
    colors = ["#A60628", "#348ABD"]

plt.plot(center_trace[:,0],label="Trace of centre_0",lw=lw,c=colors[0])
    
plt.plot(center_trace[:,1],label="Trace of centre_1",lw=lw,c=colors[1])
plt.title("Traces of unknown parameters")
leg = plt.legend(loc="upper right")
leg.get_frame().set_alpha(0.7)

###Plot setup for unknown taus###

plt.subplot(312)
std_trace=mcmc.trace("stds")[:]
plt.plot(std_trace[:,0],label="Trace of tau_0",c=colors[0],lw=lw)
plt.plot(std_trace[:,1],label="Trace of tau_1",c=colors[1],lw=lw)
plt.legend(loc="upper right")

###Trace of prioris to cluster, k=0.###
plt.subplot(313)
x_trace = mcmc.trace("x_")[:]
plt.plot(x_trace,label="p(k_0) ",color="#467821",lw=lw)
plt.title("Assignment of prioris to cluster k_0")
plt.xlabel("Steps")
plt.ylim(0,1)
plt.legend()

#plt.show()
figsize(11.0,4)

#Plots of posterior dist. of unknowns.

_i = [1,2,3,4,5,6]

for i in range(2):
    plt.subplot(3,2,_i[2*i])
    plt.title("Posterior of centres %d"%i)
    plt.hist(center_trace[:,i],color =colors[i],bins=30,histtype="stepfilled" )
    
    plt.subplot(3,2,_i[2*i +1])
    plt.title("Posterior of s_devs %d"%i)
    plt.hist(std_trace[:,i],color=colors[i],bins=30,histtype="stepfilled")
    
    ## Now we plot the posterior labelling of data points as done in the assignement phase.
    if i ==0:
        pass
    elif i==1:
        plt.subplot(3,2,_i[3*i+1])
        cmap = mpl.colors.LinearSegmentedColormap.from_list("BMH",colors)
        assign_trace = mcmc.trace("Assignement")[:]
        plt.scatter(data,1- assign_trace.mean(axis=0),cmap=cmap,
                    c=assign_trace.mean(axis=0),s=50)
        plt.ylim(-0.05,1.05)
        plt.xlim(35,300)
        plt.title("Probability of data point belonging to cluster 0")
        plt.ylabel("probability")
        plt.xlabel("value of data point") 
        #print len(assign_trace.mean(axis=0))#300
        
        # We now overlay the histogram data set using the posterior mean parameters.
        
        X = np.linspace(20,300,500) # Make 500 equally spaced 1d values.
        #norm = stats.norm
        # Call mean values.
        center_mean = center_trace.mean(axis=0)
        sdev_mean = std_trace.mean(axis=0)
        posterior_mean = mcmc.trace("x_")[:].mean() # Just a scalar value.
        plt.subplot(3,2,6)
        plt.hist(data,bins=20,histtype="stepfilled",normed=True,color="k",lw=2,label="Data histogram")
        
        y = posterior_mean * norm.pdf(X,loc=center_mean[0],scale=sdev_mean[0])
        plt.plot(X,y,label="Cluster 0 using posterior mean parameters",lw=6)
        plt.fill_between(X,y,color=colors[0],alpha=0.3)
        
        y = (1 - posterior_mean) * norm.pdf(X,loc=center_mean[1],scale=sdev_mean[1])
        plt.plot(X,y,label="Cluster 1 using posterior mean parameters",lw=6)
        plt.fill_between(X,y,color=colors[1],alpha=0.3)
        plt.legend(loc="upper left")
        plt.title("Visualizing Clusters using posterior-mean parameters");

        plt.tight_layout()
    
        
        


plt.show()