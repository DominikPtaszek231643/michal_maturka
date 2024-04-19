odd_num = []
even_num = []

with open('pi_przyklad.txt') as file:
    content = file.readlines()

#program zlicza liczbę wszystkich nieparzystych i wszystkich parzystych

    for i in range(0,len(content),1):
        number1 = content[i].strip()
        if number1 == '0' or number1 == '2' or number1 == '4' or number1 == '6' or number1 =='8':
            even_num.append(int(number1))
        elif number1 == '1' or number1 == '3' or number1 == '5' or number1 == '7' or number1 == '9':
            odd_num.append(int(number1))
print(odd_num)
num_0 = even_num.count(0)
num_2 = even_num.count(2)
num_4 = even_num.count(4)
num_6 = even_num.count(6)
num_8 = even_num.count(8)
num_1 = odd_num.count(1)
num_3 = odd_num.count(3)
num_5 = odd_num.count(5)
num_7 = odd_num.count(7)
num_9 = odd_num.count(9)

print(f'Liczba cyfr nieparzystych to: {len(odd_num)}, a liczba cyfr parzystych to: {len(even_num)}')
print(f'Ilość 0 to:{num_0}')
print(f'Ilość 1 to:{num_1}')
print(f'Ilość 2 to:{num_2}')
print(f'Ilość 3 to:{num_3}')
print(f'Ilość 4 to:{num_4}')
print(f'Ilość 5 to:{num_5}')
print(f'Ilość 6 to:{num_6}')
print(f'Ilość 7 to:{num_7}')
print(f'Ilość 8 to:{num_8}')
print(f'Ilość 9 to:{num_9}')