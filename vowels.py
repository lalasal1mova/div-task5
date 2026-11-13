a = str(input("Enter a word or a sentence: "))
sait = ['a', 'e', 'ə', 'ı', 'i', 'o', 'ö', 'u', 'ü']
count = 0
a = a.lower()

for i in a:
    for j in sait:
        if i == j:
            count +=1

print(f"Saitlerin sayi: {count}")