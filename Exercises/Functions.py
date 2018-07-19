'''
@author: laptop
'''
#
# Example file for working with functions
#

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


"""
In the first function below, a second argument isn't passed. So the default
value is used instead which is 1.
"""
print (power(2))
print (power(2, 3))


