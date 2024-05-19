with open("instrukcje.txt") as file:
    content = file.readlines()
    for i in range(0, len(content), 1):
        content[i] = content[i].strip()

    counter = 0
    max_occur = -1
    current_command = None
    max_occur_word = None
    for i in range(0, len(content), 1):

        current_word = content[i].split(' ')[0]

        if current_command is None:
            current_command = current_word
            counter += 1

        elif current_word == current_command:
            counter += 1
        elif current_word != current_command:

            if counter > max_occur:
                max_occur = counter
                max_occur_word = current_command
            counter = 1
            current_command = current_word

    print(max_occur_word, max_occur)
