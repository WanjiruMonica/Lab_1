# A program that asks for user input and finds sum and average of the numbers


def main():
    sum = 0

    for i in range(5):
        num = int(input("Enter a value: "))
        sum = sum + num

    average = (sum)/5
    print("The sum of the above values is",sum,"while the average is",average)

main()
