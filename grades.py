students = [("Aysel", 95), ("Murad", 72), ("Leyla", 84), ("Elvin", 48), ("Nigar", 63)]

for list in students:
    bal = ''
    if list[1] > 90:
        bal = 'A'

    elif list[1] > 80:
        bal = 'B'

    elif list[1] > 70:
            bal = 'C'

    elif list[1] > 60:
            bal = 'D'

    elif list[1] > 50:
            bal = 'E'

    else:
          bal = 'F'

    print(f"{list[0]}: {list[1]} -> {bal}")