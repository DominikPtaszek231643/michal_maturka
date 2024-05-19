def funkcja(number1, number2):
    for j in range(2, int(number1), 1):
        if int(number1) % j == 0 and int(number2) % j == 0:
            return False
    return True


with open('liczby.txt') as file:
    content = file.readlines()
    for i in range(0, len(content), 1):
        content[i] = content[i].strip()
    counter2 = 0
    for i in range(0, len(content), 1):
        current_number = content[i]
        splitted_text = current_number.split(' ')[0]
        splitted_text2 = current_number.split(' ')[1]

        if funkcja(splitted_text,splitted_text2):
            counter2 += 1

    print(counter2)