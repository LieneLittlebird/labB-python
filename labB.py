# Liene Putniņa, lr12022
# B12. Given a natural number n. Find the Fibonachi number f(n).
# Create and use a function to calculate the Fibonachi number f(n).
# (Fibonachi numbers are f(1) = 1, f(2) = 1, f(n) = f(n-1) + f(n-2), t. i. f(3)=2, f(4)=3, f(5)=5 utt.).
# Also, check if the given number n is a Fibonachi number.
# Create and use a function for this check.
# Program created at: 2021/26.03

# A recursive function finds the nth Fibonacci term.
# It checks the entered number and returns the sum of the two previous numbers in
# the Fibonacci sequence, if the number is not smaller or equal to 1 (0 and 1 ar the first two Fibonacci numbers)
def findFibonacci(n):
    if n <= 1:
        return n
    else:
        return findFibonacci(n - 1) + findFibonacci(n - 2)

# A function checks, if the entered number is a Fibonacci number.
# It starts with 0 and 1, since those are the first two Fibonacci numbers.
# They are added to each other to get their Fibonacci number.
# Then a while loop is executed, which stops only when the variable "next" is not smaller than the input number.
# In each iteration the variables are assigned a new value thus incrementing the initial
# number and getting to the next term in the Fibonacci sequence.
# If next (each Fibonacci number) is equal to the input number, the input number IS a Fibonacci number.
# If not, it is NOT a Fibonacci number.
def isFibonacci(n):
    if n <= 1:
        print(f"{n} is a Fibonacci number.\n")
    else:
        a = 0
        b = 1
        next = a + b

        while next < n:
            a = b
            b = next
            next = a + b

        if next == n:
            print(f"{n} is a Fibonacci number.\n")
        else:
            print(f"{n} is NOT a Fibonacci number.\n")

# Input validation function to keep the execution loop cleaner
# This function will be called each time an input is needed. 
def getInput(): 
    inputNumber = None 
    continueEntering = True
    while continueEntering:
        try:
            inputNumber = int(input()) 
            assert inputNumber >= 0
        except ValueError:
            print("Invalid input. Please, enter an integer.")
            continue
        except AssertionError:
            print("Invalid input. Please, enter a positive integer.")
        else:
            continueEntering = False
    
    return inputNumber

# A function for exercise one (finding the Fibonacci numbers).
# This function deals with the input/output of the exercise and
# executes the function to find the Fibonacci term for the input number.
def exerciseOne():
    print("Enter a number to get the nth Fibonacci term:")
    n = getInput()
    fibonacciNumber = findFibonacci(n)
    print(f"The Fibonacci term Nr.{n} is {fibonacciNumber}\n")

# A function for exercise two (checking if the input is a Fibonacci number).
# This function deals with the input/output of the exercise and
# executes the function to check if the input is a Fibonacci number.
def exerciseTwo(): 
    print("Enter a number to see if it is a part of the Fibonacci sequence: ")
    n = getInput()
    isFibonacci(n)

# Execution of the program
repeatExec = True
while repeatExec:
    exerciseOne()
    exerciseTwo()

    print("Enter 1 to continue or 0 to quit")
    continueExec = getInput()

    if continueExec == 0:
        repeatExec = False
        break

    else:
        repeatExec = True
