def funkcja(number):
    for j in range(2, int(number), 1):
        if int(number) % j == 0:
            return False
    return True


with open('Dane_2203/liczby_przyklad.txt') as file:
    content = file.readlines()
    for i in range(0, len(content), 1):
        content[i] = content[i].strip()
    counter2 = 0
    for i in range(0, len(content), 1):
        current_number = content[i]
        splitted_text = current_number.split(' ')[0]

        if funkcja(splitted_text):
            counter2 += 1

    print(counter2)
