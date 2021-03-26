# Liene Putniņa, lr12022
# B12. Given a natural number n. Find the Fibonachi number f(n).
# Create and use a function to calculate the Fibonachi number f(n).
# (Fibonachi numbers are f(1) = 1, f(2) = 1, f(n) = f(n-1) + f(n-2), t. i. f(3)=2, f(4)=3, f(5)=5 utt.).
# Also, check if the given number n is a Fibonachi number.
# Create and use a function for this check.
# Program created at: 2021/26.03

#1. Define n and sort out its usage
#2. Write validation function (negative also)


def findFibonacci(n):
    # n = int
    if n <= 1:
        return n
    else:
        return findFibonacci(n - 1) + findFibonacci(n - 2)

def isFibonacci(n):
    # n = int
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
            print(f"{n} is NOT  a Fibonacci number.\n")

def getInput: 
    inputNumber = 0 #Does it work like that?
    continueEntering = True
        while continueEntering:
            try:
                inputNumber = int(input()) #Does it work like that?
                assert inputNumber > 0
            except ValueError:
                print("Invalid input. Please, enter an integer.")
                continue
            except AssertionError:
                print("Invalid input. Please, enter a positive integer.")
            else:
                continueEntering = False

def exerciseOne:
    findFibNum = int(input("Enter a number to get the nth Fibonacci term: "))
    fibonacciNumber = findFibonacci(n)
    print(f"The Fibonacci term Nr. {n} is {fibonacciNumber}")
    
def exerciseTwo:
    checkFibNum = int(
        int(input("Enter a number to see if it is a part of the Fibonacci sequence: "))
    )
    print(isFibonacci(n))

repeatExec = True
while repeatExec:
    print(exerciseOne())
    print(exerciseTwo())

    count(int(input("Enter 1 to continue or 0 to quit \n"))) #Add validation somehow
    if count == 0:
        repeatExec = False
        break
    else:
        repeatExec = True
