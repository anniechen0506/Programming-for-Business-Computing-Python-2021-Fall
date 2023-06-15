no_arrange_list = []
arranged_list = []
company_list = []
num_list = []
storage = []
final_list = []

with open(file=input(), mode='r', encoding='utf-8') as f:
    for line in f:
        info = line.split(',')
        no_arrange_list.append(info)

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

for x in range(len(company_list)):
    for y in range(len(company_list[x])):
        company_list[x][y] = company_list[x][y].strip()
        company_list[x][y] = company_list[x][y].strip("\n")

for x in range(len(company_list)):
    for y in range(8,15): # 行業代號
        if (company_list[x][y] and company_list[x][y+1] != ""):
            if y % 2 == 0:
                if int(company_list[x][y]) not in num_list:
                    num_list.append(int(company_list[x][y]))
                    storage.append(int(company_list[x][y]))
                    storage.append(company_list[x][y+1])
                    storage.append(company_list[x][4])  # 資本額
                    storage.append(1)  # 計算數量
                    final_list.append(storage)
                    storage = []
                elif int(company_list[x][y]) in num_list:
                    for a in range(len(final_list)):
                        if int(company_list[x][y]) in final_list[a]:
                            final_list[a][2] += ("," + company_list[x][4])
                            final_list[a][3] += 1  # 計算數量

# print(final_list)

for i in range(len(final_list)):
    final_list[i][0] = int(final_list[i][0])
    final_list[i][2] = final_list[i][2].split(",")

for i in range(len(final_list)):
    for j in range(len(final_list[i][2])):
        final_list[i][2][j] = int(final_list[i][2][j])  # 資本額轉成整數

# 計算中位數
for i in range(len(final_list)):
    final_list[i][2].sort()
    n = len(final_list[i][2])
    if (n % 2) != 0:
        final_list[i][2] = final_list[i][2][int((n+1)/2)-1]
    else:
        median = (final_list[i][2][int(n/2)-1] + final_list[i][2][int((n/2))]) / 2
        new_median = f"{median:.0f}" 
        final_list[i][2] = int(new_median)

final_list.sort(key = lambda x:(-x[2],x[0]))

for i in range(len(final_list)):
    if i == 10:
        break
    else:
        print(f"{final_list[i][0]:06d}" + " " + "("
            + final_list[i][1] + "):" + " " + "$"
            + str(final_list[i][2]) + ";" + " " + "N="
            + str(final_list[i][3]))
