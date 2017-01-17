def fact(n):
    if type(n) == complex:
        raise Exception("Cannot calculate complex number!")
    
    if (n==1):
        return 1
    elif(n < 0):
        raise Exception("Cannot find negative factorial!")
    return n * fact(n-1)

if __name__=="__main__":
    for i in range(1,10+1):
        print ("%d! = %g"%(i,fact(i)))
        print ("%d! = %g"%(-5,fact(-5)))
        t = 5 - 4j
        print ("%d! = %g"(t,fact(t)))