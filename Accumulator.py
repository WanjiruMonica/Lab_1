# This function computes the factorial of the number entered by a user


def factor():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(1,n+1):
        fact = fact * 5 # this will find answer of 5 to the power of value entered.
        print("The factorial of", n, "is", fact)


factor()
