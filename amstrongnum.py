num = int(input("Enter a number: "))
x = num
sum = 0

while num > 0:
    d = num % 10
    num = num // 10
    sum = sum + (d * d * d)

if x == sum:
    print("The number", x, "is an Armstrong Number")
else:
    print("The number", x, "is not an Armstrong Number")
