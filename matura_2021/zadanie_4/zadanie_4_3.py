with open("przyklad.txt") as file:
    content = file.readlines()
    content2 = []
    counter = 0
    for i in range(0, len(content), 1):
        content[i] = content[i].strip()
        if "DOPISZ" in content[i]:
            content2.append((content[i]))

    for i in range(0, len(content2), 1):
        content2[i] = content2[i].split(' ')[1]

    counter = 0
    max_counter = -1
    current_letter = None
    max_counter_letter = None
    # nazwa_slownika["nazwa_kluczu"] = nowa_wartosc
    dictionary = {}
    for i in range(0, len(content2), 1):
        current_letter = content2[i]

        if current_letter not in dictionary.keys():
            dictionary[current_letter] = 0

        dictionary[current_letter] += 1
# max_val = -1
#     for lst in dictionary.items():
#         print(lst)
#         key, val = lst[0], lst[1]
#
#         if

    # for i in range(0, len(content2), 1):
    #     current_letter_in_content = content2[i]
    #     if current_letter is None:
    #         current_letter = current_letter_in_content
    #         counter += 1
    #     elif current_letter == current_letter_in_content:
    #         counter +=1
    #     elif current_letter != current_letter_in_content:
    #         if counter > max_counter:
    #             max_counter = counter
    #             max_counter_letter = current_letter
    #         counter = 1
    #         current_letter = current_letter_in_content
    #
    # print(max_counter, max_counter_letter)
