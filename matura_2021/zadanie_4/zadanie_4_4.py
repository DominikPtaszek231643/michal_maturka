def provide_new_letter(letter):
    print(letter)
    ascii_code = ord(letter)

    if ascii_code == 122:
        return chr(97)

    return chr(ascii_code + 1)


with open("przyklad.txt") as file:
    content = file.readlines()
    counter = 0
    word_final = []
    # pop

    for i in range(0, len(content), 1):
        content[i] = content[i].strip()

    for i in range(0, len(content), 1):
        current_command = content[i]
        current_letter = current_command.split(" ")[1]
        if "DOPISZ" in current_command:
            word_final.append(current_letter)
        elif "USUN" in current_command:
            word_final.pop()
        elif "ZMIEN" in current_command:
            word_final.pop()
            word_final.append(current_letter)
        elif "PRZESUN" in current_command:
            for j in range(0, len(word_final), 1):
                current_letter_in_word_final = word_final[j]
                if current_letter == current_letter_in_word_final:
                    res = provide_new_letter(current_letter.lower())

                    print('To jes res'  , res)
                    word_final[j] = res.upper()
    print(word_final)