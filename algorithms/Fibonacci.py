# Demonstration of tail-recursion algorithm to yield Fibonacci numbers.

def Fibo(n,k,fibk,fibk1):
    counter=0
    if (n==k): # Base step. Stop when k reaches n.
        return fibk
    else:
        counter+=1
        return Fibo(n,k+1,fibk+fibk1,fibk)
a = Fibo(6,1,1,0)
print a
        