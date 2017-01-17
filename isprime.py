# Code to check whether input number,n, is prime.
# Prime numbers are only divisible by itself, and one.
# Thus, we run our range starting at 2, instead of one!
import pandas as pd

def Check_prime(n):
    IsPrime=False
    if n==1: # Ignore trivial case 1.
        return 0 
    else: # For all other numbers including 2.
        s =0
        for t in range(2, n+1 ):
            if (n%t) == 0:
                s+= 1 # Count instances with no remainder, if s=1 then prime else not.
        if s==1:
            #print "This is a prime number."
            IsPrime=True
        return IsPrime, t

lists= [Check_prime(x) for x in range(2,100,1)]
s1 = pd.DataFrame(lists,index=[t for t in range(2,100,1)])

print s1
# To do: Count instances of F/T no.s 