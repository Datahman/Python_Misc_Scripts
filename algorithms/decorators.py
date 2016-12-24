# Demonstration of function decorators.
import datetime

def test_time(original_func):
    def inner_func(*args, **kwargs):
        before = datetime.datetime.now()
        x = original_func(*args, **kwargs)
        after = datetime.datetime.now()
        print "Elapsed Time = {0}".format(after-before)
        return x
    return inner_func()

# Note the syntactic sugar '@'. Equivalent statement: timed_f = test_time(func) 

@test_time
def func():      
    def func1():
        print ("This is inner function")
    def add(a,b):
        c = a+b
        return c
    def minus(a,b):
        c = a-b
        return c
    print ("This is outside function")
    return func1(), add(1,5), minus(1,5)


# Advanced decorators, using details from python_notes.


# Check admin priviliges
def requires_admin(fn):
    def ret_fn(*args, **kwargs):
        
        lPermissions = get_permissions(current_user_id())
        if 'administrator' in lPermissions:
            return fn(*args, **kwargs)
        else:
            raise Exception ("Not allowed")
            
    return ret_fn
    
    
# Check logged in priviliges.

def requires_logged_in(fn):
    def ret_fn(*args, **kwargs):
        lPermissions = get_permissions(current_user_id())
        if 'logged_in' in lPermissions:
            return fn(*args,**kwargs)
        else:
            raise Exception ("Not Allowed")
    return ret_fn
    
def requires_premium_member(fn):
    def ret_fn(*args, **kwargs):
        lPermissions = get_permissions(current_user_id())
        if 'premium_member' in lPermissions:
            return fn(*args, **kwargs)
            
        else:
            raise Exception ("Not Allowed")
    return ret_fn
    
@requires_admin
def delete_user(iUserID):
    """
    some action 
    """
@requires_logged_in
def new_game():
    """
    
    """
@requires_premium_member
def make_checkpoint():
    """
    """
    
# Single decorator for all, usin above example!
    
def requires_permission(sPermission):# returns a decorator.
    def decorator(fn):
        def decorated(*args, **kwargs):
            lPermissions = get_permissions(current_user_id()) 
            if sPermission in lPermissions:
                return fn(*args, **kwargs)
            raise Exception ("Permission denied")
        return decorated
    return decorator
        
        
def get_permissions(iUserId):
    return ['logged_in']

def current_user_id():
    return 1
    
# Now decorate...

@requires_permission('administrator')
def delete_user(iUserId):
    """
    """
@requires_permission('logged_in')
def new_game():
    return "Game works!"
    
@requires_permission('premium_member')
def premium_checkpoint():
    """
    """
#premium_checkpoint()
print(new_game())


def decorator(some_f):
    def wrapper():
        num =10
        if num ==10:
            print ("Yes!")
        else:
            print ("No")
            
        some_f()
        
        print("Function has been wrapped/decorated!")
        
    return wrapper
    
@decorator
def some_func():
    print "This function is to be wrapped!"

some_func() # Equicalently -> try_decorator = decorator(some_func), try_decorator() 


# More real world examples of Python decorators.

# Example 1: Time the sum of 'n' numbers.

def timer(fn):
    def wrapper():
        t1 = datetime.datetime.now()
        fn()
        t2 = datetime.datetime.now()
        print ("Time took to execute the function: {0}").format(t2-t1)
    return wrapper
@timer
def sum_n():
    num_ = []
    for i in range(1,1000):
        num_.append(i)
    print("\n Sum of 1000 numbers is: " + str(sum(num_)) )
sum_n()

# Example 2: Limit print rate by using a time-delay wrapper.
from time import sleep
from functools import wraps
def time_delay(func):
    @wraps(func)
    def wrapper1(*args, **kwargs):
        sleep(1)
        return func(*args, **kwargs)
    return wrapper1

@time_delay
def print_n(num):
    """ Doc_string to pass """
    return num
for i in range(1,9):
    print(print_n(i))
    
# Example 3 (Most used): Check login priviliges.
print (print_n.__name__) # returns name of passed function i.e print_n.
print (print_n.__doc__) # returns dos_string as stated on print_n. 

# Above demonstrates use of wrap method to retain decorated function attributes.

# Example 4: Demonstration of N-many decorators.


    

def N_decorator(*exp_args): # print exp_args # returns ('one','two')
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            for i in exp_args:
                if i == 'one':
                
                    print "\n First list member"
                if i == 'two':
                    
                    print "\n Second list member"
            return func(*args, **kwargs) # Here call my main- function, after decoration.
        return decorated
    return decorator

@N_decorator('one','Two') # are the to be passed parameters.
def add_func():
    a=10
    b=15
    print ("\n Main function that adds to {0}").format(a+b)
    return 
add_func()
