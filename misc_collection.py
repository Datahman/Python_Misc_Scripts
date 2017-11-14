# Miscellaneous data sorting work.
import cProfile
import random
import timeit
import os
# Find largest number of the two.

def largest_num (a,b,c):
    biggest = a
    if biggest < b:
        biggest = b
    if biggest < c:
        biggest = c
    print biggest 
    
a = largest_num (5,3,6)
    
def list_largest (list_):
        biggest = list_[0] # Set first list value as largest.
        for x in list_:
            if x > biggest:
                biggest = x
        print biggest
list_largest([8,5,20,3])


# Insertion sort algorithm.


def insertion_sort(list_):
    
    for i in range(1,len(list_)):
        key = list_[i]
        j = i - 1
        
        while ((j>=0) and (list_[j] > key)):
            
            list_[j],list_[j+1] = list_[j+1],list_[j] 
            
            j = j-1
        
    print list_

#random_list= [random.randrange(1,101,1) for x in range(10)]
#cProfile.run('insertion_sort([random.randrange(1,101,1) for x in range(10)])') # Test random list elements.



# Ways to reverse a string.

string = "Word"

# Method 1: Simply print (string[::-1])
def short_reverse(new_string):
    return new_string[::-1]


empty=[]
# Method 2: 
for i in range(1,len(string)+1):
    j = -i
    empty.append(string[j])
    if i ==4:
        print(''.join(empty))
    

# Method 3: Best practice.

def reverse_string(input_string):
    new_string = []
    index = len(input_string)

    while index:
        index -= 1
        new_string.append(input_string[index])
    return ''.join(new_string)        
b = reverse_string("dummy")
#print (b)    
#print (min(timeit.repeat(lambda: reverse_string('aman' * 10 ))))
#print (min(timeit.repeat(lambda: short_reverse('aman' * 10 ))))

# Determine unique character in a string.

def unique_finder(some_string):
    length = len(some_string)
    n = 0
    while length:
        length -= 1
        n += 1
         
    return some_string[length]
print (unique_finder("lee"))

# This function returns files, and path of a given directory.
from os.path import isfile, join
cwd = os.getcwd()
def print_dir_files(cwd):
    dir_list = os.listdir(cwd) # returns all the contents as a list.
    onlyfiles = [x for x in os.listdir(cwd) if isfile(join(cwd,x)) ]
    
    print onlyfiles
a = print_dir_files(cwd)

a1 = dict(zip(('a','b','c'),(0,2,1)))
a2 = range(6) # Range is a generator!
a3 = sorted([x for x in a2 if x in a1])
a4 = sorted([a1[s] for s in a1])
a5 = [[i,i*i] for i in a2]
print a1, a2, a3, a4, a5


# Check if a given sub-string is present within a bigger list, if found add +1 to count.
#x = [1,2,4,1,2,3,2,1]
#x_1 = [1,2,4]
a, b = 9,3
x = [random.randrange(a) for __in in range(a)] 
x_1 = [random.randrange(b) for __in in range(b) ]
#print list_ , sub_list
#0:2, 3:5 (3i,3i+2)

def sub_finder(x, x_1):
    leng  = len(x)
    count = 0
    
    for i in range(0,3):
        t = x[(3*i):(3*i+2)]
        s = x_1[(3*i):(3*i+2)]
        if s==t:
            position = (3*i,i+2)
            count +=1
            message = "Match found! at position"
            print '%s %s' % (message, position)
                        
    return count, x_1, x

fun =  lambda x,x_1: sub_finder(x,x_1 )
print fun(x,x_1)


import random
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
    a = [2,1,3,2,2,2,1]
    b = [3,2,2]
    for i in range(len(a)):
        x = a[i:(len(b)+i)]
        count = 0
        if x ==b:
            position = (i,(len(b)+i-1))
            msg = "Match found! Between main positions "
            count+=1
            print  "%s %s" % (msg, position)  
    return
a = func()

# Another way of finding factorials
def factor(n):
    res = n
    for i in range(n-1,0,-1):
        res =  res * i    
    return res
print (factor(5))           


# Example: Count element differences within the list.
a = [1,2,3,5]

v = [a[i+1]-a[i] for i in range(len(a)-1)]
#print v


for i in range(len(a)-1): # 0,1,2
    print a[i+1]- a[i]



# Some ugly/ example that doesnt work!  Implementation of compwaring two strings



