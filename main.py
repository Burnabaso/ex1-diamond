def printDiamond(rows):
    for i in range(rows):
        if i ==0:
            print(""" """*(rows-1)+"*")
        else:
            print(""" """*(i-1)+"*"*i+"*"+"*"*i)
        
    
def main():
    userInput = int(input("Enter number of rows: "))
    printDiamond(userInput)
    

main()