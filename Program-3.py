a = int(input("Enter a number (a): "))
if a % 2 == 0:
    a -= 1
number = 1
for i in range(a):
    print(number, end=", " if i < a - 1 else "")
    number += 2
