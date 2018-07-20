'''

@author: laptop
'''

class myClass():
    def method1 (self):
        print ("myClass method1")

    def method2 (self, someString):
        print ("myClass method2" + someString)

"""
Inheritance in Python is denoted by placing the parent class name inside of the
child class as an argument:
"""         
class myChildClass(myClass): 

    def myChildMethod1 (self):
        print ("myChildClass method1")

    def myChildMethod2 (self, someString):
        print ("myChildClass method2" + someString)

def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")
    
    #Now since myChildClass inherits myClass, when i instantiate myChildClass,
    #I have access to the properties in both the child and parent class
    c2 = myChildClass()
    c2.method1()#From parent class
    c2.method2("This is a child method")#From parent class
    c2.myChildMethod1()#From child class
    c2.myChildMethod2("This is also a child method")#From child class

if __name__ == "__main__":
    main()    