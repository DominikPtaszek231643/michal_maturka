# Zapisz w pseudokodzie lub w wybranym języku programowania algorytm, który dla danej
# dodatniej całkowitej liczby n obliczy liczbę bloków w jej zapisie binarnym.
# Przykład:
# Dla liczby 67 wynikiem jest 3, ponieważ 67 w zapisie binarnym to 1000011 (dwa bloki jedynek
# i jeden blok zer).
# Dla liczby 245 wynikiem jest 5, ponieważ 245 w zapisie binarnym to 11110101 (trzy bloki
# jedynek i dwa bloki zer).


# while warunek jest prawdziwy:
#             0 1 2 3 4
# bin_number = '11101'
bin_number = '000000000000000000'
block_num = 1

for i in range(0,len(bin_number), 1):
    print(i,i+1,len(bin_number) )
    if  i+1<len(bin_number):
        current_number = bin_number[i].strip()
        next_number = bin_number[i+1].strip()
        if current_number == next_number:
            continue
        elif current_number!=next_number:
            block_num+=1

print(block_num)
liczbe = 4
liczba_bin = '001'
# reversed(liczba_bin)
# jak odwrocic strina super trikiem

liczba_bin = liczba_bin[::-1]
for
    liczba = liczba / 2
    reszta = liczba %2
## stworz algorytm ktory zamienia liczby dziesietne na binarne

# do domciu 2.2, 2. 3
# 2.4 dla chetnych
