

with open('bin.txt') as file:
    content = file.readlines()
    content2 = []
    block_num = 1
    block_num_2 = 0

    for i in range(0,len(content), 1):
        if  i+1<len(content):
            block_num = 0
            content2 = content[i]
            for j in range(0,len(content2),1):
                if j+1<len(content2):
                    current_number = content2[j].strip()
                    next_number = content2[j+1].strip()
                    if current_number == next_number:
                        continue
                    elif current_number!=next_number:
                        block_num+=1
            if block_num < 3:
                block_num_2+=1

    print(block_num_2)
