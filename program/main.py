
def leastSquares():
    print("\n\t Least Squares Method")
    n = int(input("\t Enter the number of data points: "))
    for i in range(n):
        x = float(input("\t Enter x: "))
        y = float(input("\t Enter y: "))
        
    sumA2 = 0
    sumB2 = 0
    sumAB = 0
    sumA = 0
    sumB = 0
    sumConstant = 0


def runProgram():
    print("\n Calculate the best fit line for a set of data points using the following methods:")
    print("\n \t 1. Least Squares Method")
    print("\t 2. ")
    print("\t 3. ")
    print("\t 4. Exit")
    userInput = int(input("\n \tWhat do you want to do? "))
    if userInput is None:
        print(userInput.isnumeric()) 
        print("Error: You must enter a number")
        runProgram()
    else:
        if userInput == 1:
            leastSquares()
        elif userInput == 2:
            print("2")
        elif userInput == 3:
            print("3")
        elif userInput == 4:
            print("\t Exit")
            exit()
