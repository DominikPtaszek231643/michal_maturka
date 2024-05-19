# x,y,z = 2,6,12
with open('liczby.txt') as file:
    content = file.readlines()
    for i in range(0, len(content), 1):
        content[i] = int(content[i].strip())
    content = list(set(content))
    content.sort()

    counter_5 = 0

    good_5 = []

    for i in range(0, len(content), 1):
        for j in range(0, len(content), 1):
            if content[j] % content[i] != 0:
                continue
            for k in range(0, len(content), 1):
                if content[k] % content[j] != 0:
                    continue
                for l in range(0, len(content), 1):
                    if content[l] % content[k] != 0:
                        continue
                    for m in range(0, len(content), 1):
                        if content[m] % content[l] != 0:
                            continue
                        elif content[i] != content[j] != content[k] != content[l] != content[m]:
                            counter_5 += 1
                            good_5.append([content[i], content[j], content[k], content[l], content[m]])

    # good_5  =list(set(good_5))

    print(counter_5, good_5)
