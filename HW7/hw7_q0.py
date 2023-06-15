no_arrange_list = []
arranged_list = []
final_list = []

with open(file = input(), mode = 'r', encoding = 'utf-8') as f:
    for line in f:
        info = line.split(',')
        no_arrange_list.append(info)

# 檢查list內容
# print(no_arrange_list)

number = int(input())
for i in range(len(no_arrange_list)):
    finish = False
    for j in range(len(no_arrange_list[i])):
        if j < (len(no_arrange_list[i])-2):
            if finish == True:
                break
            else:
                if (('"' in no_arrange_list[i][j]) and
                    ('"' not in no_arrange_list[i][j-1]) and
                    ('"' not in no_arrange_list[i][j+1])):
                    arranged_list.append(no_arrange_list[i][0].strip('""'))
                    arranged_list.append(no_arrange_list[i][1].strip('""'))
                    arranged_list.append(no_arrange_list[i][3].strip('""'))
                    final_list.append(arranged_list)
                    arranged_list = []
                    finish = True

                elif (('"' in no_arrange_list[i][j]) and
                	  ('"' in no_arrange_list[i][j+1])):
                    information = (no_arrange_list[i][j] + "," +
                                   no_arrange_list[i][j+1]).strip('""')
                    arranged_list.append(information)
                    arranged_list.append(no_arrange_list[i][2].strip('""'))
                    arranged_list.append(no_arrange_list[i][4].strip('""'))
                    final_list.append(arranged_list)
                    arranged_list = []
                    finish = True
#print(final_list)

print("營業人名稱:", final_list[number-1][2])
print("統一編號:", final_list[number-1][1])
print("營業地址:", final_list[number-1][0])
