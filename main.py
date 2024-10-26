# O(rows),rows being the input given by user
def printDiamond(rows):
    # O(rows), rows being the number of iterations based on input
    for i in range(1,rows+1):
        # print(" "*(rows-i)+"*"*((2*i)+1)) starts from 3 *
        print(" "*(rows-i)+"*"*((2*i)-1))  #starts from 1 *
        
    # O(rows-1), rows-1 being the number of iterations based on input
    for i in  range(rows-1,0,-1):
        # the middle row will be deleted since rows-i =0
        print(" "*(rows-i)+"*"*((2*i)-1))
        
    
def main():
    try:
        userInput = int(input("Enter number of rows: "))
        printDiamond(userInput)
    except:
        print("Enter an integer")

main()