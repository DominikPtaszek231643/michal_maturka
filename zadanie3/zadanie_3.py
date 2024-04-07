# Znajdź liczbę wszystkich fragmentów 2-cyfrowych, które są zapisami dziesiętnymi liczb
# o wartościach większych od 90.

#  Dla danych zapisanych w pliku pi_przyklad.txt poprawna odpowiedź to 13

# importowanie danych

# wczytywanie danych do pliku

# zaczniemy od stworzenia pojemnika na naszę dane, czyli listy

data = []

# musimy otworzyć plik pi_przyklad.txt i zacząć sczytywać z niego kolejne wiersze

# with open(nazwa_pliku.txt, tryb wczytywania(czy my chcemy tylko wczytać, czy chcemy wczytać i nadpisać, czy chcemy tylko edytować itp. ) as file:
# domyslna wartosc wczytania pliku to 'r' czyli read

# def dodaj_liczby(number1, number2):
#     return number1 + number2

counter = 0

with open('pi.txt') as file:
    content = file.readlines()

    # print(content)
    # czy wiesz jak sprawdzic listy ?

    # type()-> sprawdza typ zmiennej i używamy ją type(nazwa_zmiennej)
    # print(type(i))

    for i in range(0, len(content)-1, 1):
        # print(i)
        # i -> numer rozdzialu
        # print(content[i])
        # zamienic tekst (content[i]) na liczbę i zapisz to w zmiennej , number

        # 9, 7 =   '9' + '7' = int('97')
        # print(f'i: {i}  , i +1 :{i +1}' )
        number1 = content[i].strip()
        number2 = content[i+1].strip()

        # 9\n -> metoda .strip() -usuwa wszystkie \n, \t,
        if int(number1) ==  9 and int(number2) != 0:

            number3 = int(number1+number2)
            # print(number3)
            counter+=1
    print(counter)





        # print(type(content[i])) #-> czyli to jest tekst a my chcemy liczby , czyli musimy zamienic teskt na liczbe



    # concatenate = dodwać

    # przejdz przez cala liste content przy uzycia fora


# wiersz 1:teskt 11111111111111111111 \n
# wiersz 2:sahdshdgagdhsh \n
# print('to jest wiersz 1 dsdhsadshhas \n to jest juz jest wiersz 2 ')