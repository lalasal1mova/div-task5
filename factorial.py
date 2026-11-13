n = int(input("Enter a number: "))
fac = 1

if n < 0:
    print("Menfi ededin faktoriali yoxdur")

elif n == 0:
    print("0! = 1")

else:
    for i in range(1, n + 1):
            fac *= i

    print(f"{n}! = {fac}")