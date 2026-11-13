temperatures = [-3, 2, 8, 15, 22, 27, 31]

for i, value in enumerate(temperatures):
    weather = ''
    if value >= 30:
        weather = 'Cox isti'

    elif value >= 20:
        weather = 'Isti'

    elif value >= 10:
        weather = 'Mulayim'

    elif value >= 0:
        weather = 'Soyuq'

    else:
        weather = 'Saxta'

    print(f"{i + 1} - ci gun: {value}◦ -> {weather}")