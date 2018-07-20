'''
@author: laptop
'''
def main():
    x, y = 100, 100
    
    #Traditional if statement:
    if (x<y):
        st = "x is less than y"
        
    elif (x == y):
        st = "x is the same as y"
        
    else:
        st = "x is greater than y"
       
        
    print (st)
    
    #A more compact version of the if statement:
    st = "x is less than y" if (x<y) else "x is greater than or the same as y"
    print (st)
    
if __name__ == "__main__":
    main()