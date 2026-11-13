password = str(input("Enter your password: "))
up_count = 0
low_count = 0
digit_count = 0
symbol_count = 0

for i in password:
    if i.isdigit():
        digit_count += 1

    elif i.isalpha():
        if i.isupper():
            up_count += 1

        else:
            low_count += 1

    else:
        symbol_count += 1

print(f"Boyuk herf: {up_count}")
print(f"Kicik herf: {low_count}")
print(f"Reqem: {digit_count}")
print(f"Diger simvol: {symbol_count}")

if len(password) > 8 and (up_count > 0 and low_count > 0 and digit_count > 0 and symbol_count > 0):
    print("Guclu sifre")

else:
    print("Zeif sifre")