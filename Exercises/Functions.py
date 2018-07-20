'''
@author: laptop
'''
#
# Example file for working with functions
#
# from test.ssl_servers import args

# define a basic function


# function that takes arguments


# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result*num
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result +=x
    return result

"""
In the first function below, a second argument isn't passed. So the default
value is used instead which is 1.
"""
print (power(2))
print (power(2, 3))

"""
Passing multiple arguments within the function call:
"""
print (multi_add(2,2,2,2,2))



