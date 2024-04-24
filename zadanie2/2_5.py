with open('bin_przyklad.txt') as file:
    content = file.readlines()
    content2 = []
    content3 = []
    content4 = []
    dec_num = []
    answer = ''
    zero = [0]
    final_answer = []
    for i in range(0,len(content), 1):
        current_num = content[i]
        dec_num.append(int(current_num,2)//2)
    for j in range(0,len(dec_num),1):
        current_num_2 = dec_num[j]
        content2.append(format(current_num_2,'b'))
    for k in range(0,len(content),1):
        content3 = content[k]
        content4 = content2[k]
        while len(content3)-1 != len(content4):
            content4 = '0' + content4
        answer = ''
        for m in range(0,len(content4),1):
            if content3[m] == content4[m]:
                answer+='0'
            else:
                answer+='1'
        final_answer.append(answer)
    print(final_answer)

    with open('odp_bin_przyklad.txt') as ans_file:
        ans_file = [line.strip() for line in ans_file.readlines()
        ]
        ans_str = list(map(str,  final_answer))
        # print(ans_str, ans_file)
        print(ans_str  == ans_file )