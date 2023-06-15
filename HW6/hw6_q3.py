# version 1
passage = input()

passage = passage.replace('"', '')
passage = passage.replace(",", "")
passage = passage.replace("'", "")

passage_list = passage.split(" ")
a_list = []
f_list = []
correct_a_list = []
final_f_list = []

'''for i in range(len(passage_list)):
    for j in passage_list[i]:
        if j == "(":
            Acronym = passage_list[i]
            only_Acronym = Acronym.strip("()")
            a_list.append(only_Acronym)'''

Acronym_len = 0
for p in passage:
    if (passage.find("(") and passage.find(")")) != (-1):
        m = passage.find("(")
        n = passage.find(")")
        Acronym = passage[m + 1: n]
        a_list.append(Acronym)
        Acronym_len = len(Acronym)
        passage = passage[n + 1:]

'''Acronym_len = 0
for a in range(len(a_list)):
    Acronym_len = len(a_list[a])'''

the_order = 0
for i in range(len(passage_list)):
    for j in passage_list[i]:
        if j == "(":
            Full_Name = passage_list[i - len(a_list[the_order]): i]
            if len(Full_Name) < len(a_list[the_order]) or "" in Full_Name:
                the_order += 1
                break
            elif ((len(Full_Name) == len(a_list[the_order])) and
            ("" not in Full_Name)):
                for k in range(len(a_list[the_order])):
                    correction = True
                    if ((Full_Name[k][0].capitalize() != a_list[the_order][k])
                       or(a_list[the_order].isupper() is False)):
                        correction = False
                        break
                    '''elif (a_list[the_order].isupper() is False):
                        correction = False
                        break'''
                the_order += 1
                if correction is True:
                    f_list.append(Full_Name)
                    correct_a_list.append(a_list[the_order-1])

string = ""
for x in range(len(f_list)):
    for y in range(0, len(f_list[x])):
        if y < len(f_list[x]) - 1:
            string += (f_list[x][y] + " ")
        else:
            string += f_list[x][y]
    final_f_list.append(string)
    string = ""

for f in range(len(f_list)):
    print(correct_a_list[f] + ":", final_f_list[f])


# print(str(only_Acronym) + ":" + str(Full_Name))

# /Users/anniechen/Desktop


#version2
# 輸入
paragraph = input()

cleanParagraph = ''

# 移除標點符號
for i in range(len(paragraph)):
    if paragraph[i] != '.' and paragraph[i] != ',' and paragraph[i] != '!' and paragraph[i] != '"':
        cleanParagraph += paragraph[i]

# 用空白切割
fixedParagraph = cleanParagraph.split(' ')
cleanParagraph = []
acronym = []
fullName = []

# 移除空字串
for i in fixedParagraph:
    if i != '':
        cleanParagraph.append(i)


# 搜尋
for i, value in enumerate(cleanParagraph):
    if value[0] == '(' and value[len(value)-1] == ')':
        # 確認是不是大寫
        fit = True
        for j in value[1:len(value)-1]:
            if j.islower():
                fit = False
        if fit:
            acronym.append(value[1:len(value)-1])
            tmp = []
            for j in range(i-(len(value)-2), i):
                tmp.append(cleanParagraph[j])
            strTmp = ' '.join(tmp)
            fullName.append(strTmp)

# 印出答案
for a, f in zip(acronym, fullName):
    tmp = f.split(' ')
    fit = True
    for i in range(len(tmp)):
        if len(tmp) != len(a):
            fit = False
        elif tmp[i][0].lower() != a[i].lower():
            fit = False
    if fit:
        print(str(a)+": "+str(f))
