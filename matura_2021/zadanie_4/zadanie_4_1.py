# text =' nienawidze poniedzialkow 123'
#
#
# if "nienawidze" in text:
#     print('Jest')



with open("przyklad.txt") as file:
    content = file.readlines()
    counter = 0
    for i in range(0, len(content), 1):
        content[i] = content[i].strip()
    for i in range(0, len(content), 1):
        current_word = content[i]
        if "DOPISZ" in current_word:
            counter +=1
        elif "USUN" in current_word:
            counter -=1
    print(counter)