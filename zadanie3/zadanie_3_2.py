

data = []
array = []



with (open('pi_przyklad.txt') as file):
    content = file.readlines()
    #
    for i in range(0, 10, 1):
         for j in range(0, 10, 1):
            counter = 0
            fragment = f'{i}{j}'

            min_counter = 0
            max_counter = 0

            for k in range(0,len(content)-1,1):


                number1 = content[k].strip()
                number2 = content[k + 1].strip()
                current_fragment = number1+number2

                print(f'Fragment : {fragment} Current Fragment:{current_fragment}' , counter )

                if fragment == current_fragment:
                    counter+=1
                    print(counter)

            array.append(counter)


    min_value, min_occurences = 0,0
    max_value, max_occurences = 0,0
    for idx, counter_value in enumerate(array):
        print(f'idx: {idx} Counter: {counter_value}')
        if counter_value < min_occurences:
            min_occurences = counter_value

        if counter_value > max_occurences:
            max_occurences = counter_value
            max_value =  idx





    print(max_value, max_occurences)




    #
    # # [4,4,4]
    # print(array.index(maximum))
    # print(array.index(minimum))
    # print(f'min = {minimum} max = {maximum}')

    # liste ktora 100 dlugosci
    # lista =[] #
# in   00 01   02   03 04
    # [5,  4,  3 , 2, 1, ......]

    # lista = [0] * 100
    #
    # for text_idx in range(0, len(content) -1 ):
    #     current_number =  int(content[text_idx].strip() + content[text_idx+1].strip())
    #
    #     lista[current_number]+=1
    #
    # print(lista[62])







