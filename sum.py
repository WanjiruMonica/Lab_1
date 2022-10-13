# A program that finds the sum from 1 to value entered

def main():
    sum = 0
    n = int(input("Enter a number: "))
    
    for i in range(n+1):
        sum = sum + i
    print("The sum of numbers from 1 to",n,"is",sum)


main()
        
