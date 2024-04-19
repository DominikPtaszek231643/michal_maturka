with open('pi_przyklad.txt') as file:
    content = file.readlines()

    # program zlicza liczbę wszystkich nieparzystych i wszystkich parzystych

    even_numbers = {
        i: 0 for i in range(0, 10, 2)
    }

    odd_numbers = {
        i: 0 for i in range(1, 10, 2)
    }

    for i in range(0, len(content), 1):
        current_number = int(content[i].strip())

        if current_number % 2 == 0:
            even_numbers[current_number] += 1
        else:
            odd_numbers[current_number] += 1

    print('Liczby parzyste:', even_numbers)

    print('Liczby nieparzyste', odd_numbers)
