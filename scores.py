scores = [78, 92, 65, 88, 100, 54, 91, 73]
sum = 0
average = 0
greater_from_90 = 0
maks = scores[0]

for i in scores:
    sum += i
    if i >= 90:
        greater_from_90 += 1

    if maks < i:
        maks = i

print(f"Ballarin cemi: {sum}")
print(f"Orta bal: {sum / len(scores)}")
print(f"90 ve yuxari bal alanlarin sayi: {greater_from_90}")
print(f"Maksimum bal: {maks}")