def printDiamond(rows):
    for i in range(1,rows+1):
        # print(" "*(rows-i)+"*"*((2*i)+1)) starts from 3 *
        print(" "*(rows-i)+"*"*((2*i)-1))  #starts from 1 *
        
    
def main():
    userInput = int(input("Enter number of rows: "))
    printDiamond(userInput)
    

main()