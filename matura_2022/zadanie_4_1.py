with open('liczby.txt') as file:
    content = file.readlines()

    for i in range(0,len(content) , 1):
        content[i] = content[i].strip()



    counter = 0
    first_occurence = None
    for i in range(0,len(content), 1):
        current_num = content[i].strip()
        # print(current_num)
        # print(current_num[0], current_num[-1])
        if current_num[0] == current_num[-1]:
            counter+=1

            if first_occurence == None:
                first_occurence = current_num

    print(counter, first_occurence)