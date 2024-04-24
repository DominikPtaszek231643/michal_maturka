with open('bin.txt') as file:
    content = file.readlines()
    for i in range(0,len(content), 1):
        content[i] = int(content[i])
    max_num = max(content)
    print(max_num)