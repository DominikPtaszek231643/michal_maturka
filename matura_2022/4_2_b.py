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

        #print(f'Aktualna liczba : {current_number} Dzielnik: {divisor}')
    #print(factors)


    return factors


#
# liste = [1,2,2,3,4,5,5,5]
#
#
# unique_dividors = set(liste)
# print(len(unique_dividors))
# print(type(unique_dividors) , unique_dividors)




with open('liczby.txt') as file:
    content = file.readlines()
    len_factors = 0
    biggest_num = []
    for i in range(0, len(content), 1):
        content[i] = content[i].strip()



    for i in range(0,len(content), 1):
        current_num = content[i]
        factors = find_prime_factors(current_num)
        if len_factors <= len(factors):
            len_factors = len(factors)

    for i in range(0,len(content), 1):
        current_num = content[i]
        factors = find_prime_factors(current_num)
        if len(factors) == len_factors:
            biggest_num.append((current_num))

    print(f'Największa liczba: {biggest_num}, ilość dzielników: {len_factors}')