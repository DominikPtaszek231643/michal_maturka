numbers = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,

}

with open('pi_przyklad.txt') as file:
    content = file.readlines()

    # program zlicza liczbę wszystkich nieparzystych i wszystkich parzystych

    for i in range(0, len(content), 1):
        current_number = int(content[i].strip())

        numbers[current_number] += 1

print(numbers)
### i teraz tylko musisz to ladnie pokazac :liczby nieparzyste, liczby parzyste