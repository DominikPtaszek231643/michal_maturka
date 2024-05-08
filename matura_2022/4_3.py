def check_if_good_3(x,y,z):
    if z%y == 0 and y%x == 0 and x!=y!=z:
        return True
    else:
        return False

def check_if_good_5(u,w,x,y,z):
    if x%w == 0 and w%u == 0 and z%y == 0 and y%x == 0 and x!=y!=z!=u!=w:
        return True
    else:
        return False

# x,y,z = 2,6,12
with open('przyklad.txt') as file:
    content = file.readlines()
    for i in range(0, len(content), 1):
        content[i] = int(content[i].strip())
    content = list(set(content))
    content.sort()
    counter_3 = 0
    counter_5 = 0


    for i in range(0, len(content), 1):
        for j  in range(0, len(content), 1):
            for k in range(0, len(content), 1):
                if check_if_good_3(content[i], content[j], content[k]):
                    counter_3+=1
                    print(content[i], content[j], content[k])

    for i in range(0, len(content), 1):
        for j  in range(0, len(content), 1):
            for k in range(0, len(content), 1):
                for l in range(0, len(content),1):
                    for m in range(0,len(content), 1):
                        if check_if_good_5(content[i], content[j], content[k], content[l],content[m]):
                            counter_5+=1
                            print(content[i], content[j], content[k], content[l], content[m])
    print(counter_3, counter_5)