import datetime
no_arrange_list = []
arranged_list = []
company_list = []
sp2 = "　"

with open(file=input(), mode='r', encoding='utf-8') as f:
    for line in f:
        info = line.split(',')
        no_arrange_list.append(info)

number = input()

for i in range(len(no_arrange_list)):
    finish = False
    for j in range(len(no_arrange_list[i])):
        if j < (len(no_arrange_list[i])-2):
            if finish is True:
                break
            else:
                if (('"' in no_arrange_list[i][j]) and
                   ('"' not in no_arrange_list[i][j-1]) and
                   ('"' not in no_arrange_list[i][j+1])):
                    information = no_arrange_list[i][j].strip('"')
                    arranged_list.append(no_arrange_list[i][3].strip('"'))
                    if no_arrange_list[i][2] == '':
                        arranged_list.append(no_arrange_list[i][1])
                    else:
                        arranged_list.append(no_arrange_list[i][1]+'('+no_arrange_list[i][2]+')')
                    year = 1911 + int(no_arrange_list[i][5][0:3])
                    date = str(year) + no_arrange_list[i][5][3:5] + no_arrange_list[i][5][5:7]
                    arranged_list.append(int(date))     
                    arranged_list.append(int(no_arrange_list[i][4]))
                    arranged_list.append(information)
                    company_list.append(arranged_list)
                    arranged_list = []
                    finish = True
                    
                elif (('"' in no_arrange_list[i][j]) and
                	  ('"' in no_arrange_list[i][j+1])):
                    information = (no_arrange_list[i][j] + "," +
                                   no_arrange_list[i][j+1]).strip('"')
                    arranged_list.append(no_arrange_list[i][4].strip('"'))
                    if no_arrange_list[i][3] == '':
                        arranged_list.append(no_arrange_list[i][2])
                    else:
                        arranged_list.append(no_arrange_list[i][2]+'('+no_arrange_list[i][3]+')')	
                    year = 1911 + int(no_arrange_list[i][6][0:3])
                    date = str(year) + no_arrange_list[i][6][3:5] + no_arrange_list[i][6][5:7]
                    arranged_list.append(int(date))
                    arranged_list.append(int(no_arrange_list[i][5]))
                    arranged_list.append(information)
                    company_list.append(arranged_list)
                    arranged_list = []
                    finish = True

company_list.sort(key = lambda x:(x[2], -x[3], x[1]))

#print(company_list)

for i in range(len(company_list)):
    company_list[i][2] = str(company_list[i][2])
    company_list[i][3] = str(company_list[i][3])

'''for i in range(len(company_list)):
    print(company_list[i][2][:4])
    print(company_list[i][2][4:6])
    print(company_list[i][2][6:8])'''

for i in range(len(company_list)):
    d1 = datetime.datetime(int(company_list[i][2][:4]),int(company_list[i][2][4:6]),int(company_list[i][2][6:8]))
    the_date = d1.strftime('%Y-%m-%d')
    company_list[i][2] = the_date
    company_list[i][3] = format(int(company_list[i][3]), ',')

for i in company_list:
    if len(i[0]) < 20:
        i[0] = i[0] + sp2*(20-len(i[0]))

found_number = False
total_num = 0
for i in range(len(company_list)):  
    if number in company_list[i][1]:
        found_number = True
        if found_number is True:
            print(f"{company_list[i][0]:<20s}"+" "+f"{company_list[i][1]:<20s}"+" "
                +f"{company_list[i][2]:<20s}"+" "+f"{company_list[i][3]:<20s}"+" "
                +f"{company_list[i][4]:<20s}")
            total_num += 1
    if total_num == 20:
        break

if found_number == False:
        print("NO_DATA_FOUND")

# /Users/anniechen/Desktop
