no_arrange_list = []
arranged_list = []
company_list = []

with open(file=input(), mode='r', encoding='utf-8') as f:
    for line in f:
        info = line.split(',')
        no_arrange_list.append(info)

# 第一行先append表頭
company_list.append(no_arrange_list[0])

for i in range(len(no_arrange_list)):
    finish = False
    for j in range(len(no_arrange_list[i])):
        if j < (len(no_arrange_list[i])-1):
            if finish is True:
                break
            else:
                if (('"' in no_arrange_list[i][j]) and
                   ('"' not in no_arrange_list[i][j-1]) and
                   ('"' not in no_arrange_list[i][j+1])):
                    information = no_arrange_list[i][j].strip('"')
                    arranged_list.append(information)
                    arranged_list.append(no_arrange_list[i][1])
                    arranged_list.append(no_arrange_list[i][2])
                    arranged_list.append(no_arrange_list[i][3].strip('"'))
                    for k in range(4,16):
                        arranged_list.append(no_arrange_list[i][k])
                    company_list.append(arranged_list)
                    arranged_list = []
                    finish = True
                    
                elif (('"' in no_arrange_list[i][j]) and
                      ('"' in no_arrange_list[i][j+1])):
                    information = (no_arrange_list[i][j] + "," +
                                   no_arrange_list[i][j+1]).strip('"')
                    arranged_list.append(information)
                    arranged_list.append(no_arrange_list[i][2])
                    arranged_list.append(no_arrange_list[i][3])
                    arranged_list.append(no_arrange_list[i][4].strip('"'))
                    for k in range(5,17):
                        arranged_list.append(no_arrange_list[i][k])
                    company_list.append(arranged_list)
                    arranged_list = []
                    finish = True

# print(company_list)

max_len_list = [-99999, -99999, -99999, -99999, -99999, -99999, -99999, -99999, -99999, -99999, -99999, -99999, -99999, -99999, -99999, -99999]

for m in range(len(company_list)):
    for n in range(len(company_list[m])):
        if len(company_list[m][n].strip()) >  max_len_list[n]:
            max_len_list[n] = len(company_list[m][n].strip())
for m in range(len(max_len_list)):
    print(max_len_list[m])
