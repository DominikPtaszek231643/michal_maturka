# Otwarcie pliku z binarnymi danymi wejściowymi do odczytu
with open('bin_przyklad.txt') as file:
    final_answers = []  # Inicjalizacja listy na wyniki końcowe

    # Przetwarzanie każdej linii w pliku
    for line in file.readlines():
        current_bin_num = line.strip()  # Usunięcie białych znaków z końców linii

        # Konwersja liczby binarnej na int, dzielenie przez 2 i konwersja z powrotem na binarny (bez '0b')
        divided_bin_num = str(bin(int(current_bin_num, 2) // 2))[2:]

        # Dopisanie brakujących zer na początku, aby długość była zgodna z oryginałem
        divided_bin_num_with_zeros = '0' * (len(current_bin_num) - len(divided_bin_num)) + divided_bin_num

        answer = ''  # Inicjalizacja zmiennej na odpowiedź

        # Porównywanie każdej cyfry w oryginalnym i przesuniętym ciągu
        for index, current_bin_num_digit in enumerate(current_bin_num):
            # Jeśli cyfry są takie same, dodaj '0', jeśli różne, dodaj '1'
            if current_bin_num_digit == divided_bin_num_with_zeros[index]:
                answer += '0'
            else:
                answer += '1'

        # Dodanie wyniku dla bieżącej linii do listy wyników
        final_answers.append(answer)

# Otwarcie pliku z oczekiwanymi odpowiedziami do porównania
with open('odp_bin_przyklad.txt') as ans_file:
    answers = []  # Lista na oczekiwane odpowiedzi

    # Wczytanie odpowiedzi i usunięcie białych znaków
    for line in ans_file.readlines():
        answers.append(line.strip())

    # Porównanie wygenerowanych odpowiedzi z oczekiwanymi i wyświetlenie wyniku
    print(answers == final_answers)  # Wyświetlenie True, jeśli listy są identyczne, w przeciwnym razie False
