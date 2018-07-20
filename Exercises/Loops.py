'''

@author: laptop
'''

#While loop:
def main():
    x=0
     
    while (x<5):
        print (x)
        x +=1
 
#For loop:
for x in range(0, 10):
    print(x)
 
#For loop to iterate over a collection:
weekdays = ["Monday","Tuesday","Wednesday", "Thursday", "Friday"]
for d in weekdays:
    print (d)
     
#Breaking out of a for loop:
for x in range(0, 10):
    print (x)
    if (x==5): break

#Continuing a loop (aka skip):
for x in range(0, 10):    
    if (x % 2 == 0): continue
    print (x)
    

if __name__ == "__main__":
    main()