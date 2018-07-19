'''
@author: laptop
'''

# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
# print(f)

# # re-declaring the variable works

# f="string"
# print(f)
# # ERROR: variables of different types cannot be combined
# print("this is a string" + 123)
#But this works:
# print("this is a string " + str(123))

# Global vs. local variables in functions
def someFunction():
    f="abc"
    print(f)
    
someFunction()
print(f)
