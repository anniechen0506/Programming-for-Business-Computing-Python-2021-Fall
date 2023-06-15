count = 0
dictionary = {}
num_name_dict = {}

with open(file=input(), mode='r', encoding='utf-8') as f:
    for i in f:
        count += 1
        if count != 1:
            line = i.split('"')
            info = line[-1]
            info = info.split(',')
            num_list = []
            name_list = []
            #for j in range(len(info)):
            if info[5] != "" and info[6]!= "":
                num_list.append(info[5])
                name_list.append(info[6])
            if info[7] != "" and info[8] != "":
                num_list.append(info[7])
                name_list.append(info[8])
            if info[9] != "" and info[10] != "":
                num_list.append(info[9])
                name_list.append(info[10])
            if info[11] != "" and info[12] != "":
                num_list.append(info[11])
                name_list.append(info[12])
            for a in range(len(num_list)):
                for b in range(a):
                    #print(a,b)
                    if num_list[a] == num_list[b]:
                        continue
                    if int(num_list[a]) < int(num_list[b]):
                        if (num_list[a], num_list[b]) in dictionary.keys():
                            dictionary[(num_list[a], num_list[b])] += 1
                        else:
                            dictionary[(num_list[a], num_list[b])] = 1
                    else:
                        if (num_list[b], num_list[a]) in dictionary.keys():
                            dictionary[(num_list[b], num_list[a])] += 1
                        else:
                            dictionary[(num_list[b], num_list[a])] = 1
            for a in range(len(num_list)):
                num_name_dict[num_list[a]] = name_list[a].split("\n")[0]

number = sorted(dictionary.items(), key = lambda x:(-x[1],int(x[0][0]),int(x[0][1])))
number = number[:20]
#print(num_name_dict)

for i in range(len(number)):
    print(num_name_dict[number[i][0][0]], end = " ")
    print(num_name_dict[number[i][0][1]], end = " ")
    print(number[i][1])
