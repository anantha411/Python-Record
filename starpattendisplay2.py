print("Star Pattern Display")

num = 1
x = num

for i in range(1, 6, 1):
    num = num + 1
    for j in range(1, num, 1):
        print("*", end=" ")
    x = num + 1
    print()

print("End of Program")
