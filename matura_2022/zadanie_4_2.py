def find_prime_factors(a):
    divisor = 2
    current_number = int(a)
    factors = []
    while current_number != 1:

        if current_number % divisor == 0:

            factors.append(divisor)

            current_number = current_number // divisor
        else:
            divisor += 1

        print(f'Aktualna liczba : {current_number} Dzielnik: {divisor}')
    print(factors)
    return factors




with open('przyklad.txt') as file:
    content = file.readlines()
    len_factors = 0
    biggest_num = 0
    for i in range(0, len(content), 1):
        content[i] = content[i].strip()



    for i in range(0,len(content), 1):
        current_num = content[i]
        factors = find_prime_factors(current_num)
        if len_factors < len(factors):
            len_factors = len(factors)
            biggest_num = current_num

    print(f'Największa liczba: {biggest_num}, ilość dzielników: {len_factors}')