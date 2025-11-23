First_Number = int(input("Please enter First Number: "))
Second_Number = int(input("Please enter Second Number: "))
Limit = int(input("Number of Fibonacci Numbers to be printed: "))

print(First_Number, end=" ")
print(Second_Number, end=" ")

for i in range(Limit - 2):
    sum = First_Number + Second_Number
    First_Number = Second_Number
    Second_Number = sum
    print(sum, end=" ")
