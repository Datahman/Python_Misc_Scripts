import random
import cProfile
# Check if a given sub-string is present within a bigger list, if found add +1 to count.
#x = [1,2,4,1,2,3,2,1]
#x_1 = [1,2,4]

#print list_ , sub_list
#0:2, 3:5 (3i,3i+2)

def sub_finder():
    a, b = 9,3
    x = [random.randrange(a) for __in in range(a)] 
    x_1 = [random.randrange(b) for __in in range(b) ]
    leng  = len(x_1) # Generalise for a sub-string of arbitary length.
    count = 0
    
    for i in range(leng):
        t = x[(3*i):(3*i+3)]
        s = x_1[(3*(i-2)):(3*i+3-6)]
        if s==t:
            position = (3*i,3*i+3-1)
            count +=1
            message = "Match found! Between positions "
            print '%s %s' % (message, position)
                        
    return count, x_1, x, t, s

#for i in range(200):
#    a = sub_finder()
#    print(a)


# General case of the above method. Here for an arbiary lengths of main , and sub lists , respectively.

# Expect to find common sequence at i = 3!


def func():
    d , e = 10 , 3 
    a = [random.randrange(d) for __int in range(d)]
    b = [random.randrange(e) for __int in range(e)]
    for i in range(len(a)):
        x = a[i:(len(b)+i)]
        count = 0
        if x ==b:
            position = (i,(len(b)+i-1))
            msg = "Match found! Between main positions "
            count+=1
            print  "%s %s" % (msg, position)  
    return a, b
    
#for i in range(100):
#    a = func()
#    print (a)
cProfile.run('[func() for x in range(1)]')