#version1
width = int(input())
column_format = input().split(',')
data = []  # 輸入的資料將存於此
column_number = len(column_format)

while True:  # 可以一直輸入的迴圈
    input_data = input()
    if input_data != "RECORD_END":
        clean_data = input_data.split(',')
        data.append(clean_data)
    else:
        break

# 先宣告該欄位的型態
for i in range(len(data)):
    for j in range(len(data[i])):
        if column_format[j] == "s":
            data[i][j] = str(data[i][j])
        elif column_format[j] == "f":
            data[i][j] = float(data[i][j])

for i in range(len(data)):
    for j in range(len(data[i])):
        if type(data[i][j]) == type(" "):
            # ((column_format[j] == "s") and data[i][j].isinstance(" ")):
            # type(data[i][j]) == type(" ")):
            if len(data[i][j]) <= width:
                if j < column_number - 1:
                    print(f'{data[i][j]:>{width}s}', end=" ")
                else:
                	print(f'{data[i][j]:>{width}s}')
            elif len(data[i][j]) > width:
                # no_show = width - len(data[i][j])
                # data[i][j][0: no_show + 1] = "~"
                data[i][j] = data[i][j][0: width]
                the_list = list(data[i][j])
                the_list[width - 1] = "~"
                data[i][j] = "".join(the_list)
                # list(data[i][j])[width - 1] = "~"
                # data[i][j] = "".join(list(data[i][j]))
                if j < column_number - 1:
                    print(data[i][j][0: width], end=" ")
                else:
                    print(data[i][j][0: width])
        elif type(data[i][j]) == type(0.0):
            # ((column_format[j] == "f") and data[i][j].isinstance(0.0)):
            # type(data[i][j]) == type(0.0)):
            data[i][j] = str(data[i][j])
            data[i][j] = f'{float(data[i][j]):.2f}'
            if len(data[i][j]) <= width:
                if j < column_number - 1:
                    print(f'{float(data[i][j]):{width}.2f}', end=" ")
                else:
                    print(f'{float(data[i][j]):{width}.2f}')
            elif len(data[i][j]) > width:
                # data[i][j] = f'{data[i][j]:{width}.2f}'
                # no_show = width - len(data[i][j])
                # data[i][j][0:no_show+1] = "~"
                # data[i][j] = data[i][j][0: width]
                # list(data[i][j])[width - 1] = "~"
                # data[i][j] = "".join(list(data[i][j]))
                data[i][j] = data[i][j][0: width]
                the_list = list(data[i][j])
                the_list[width - 1] = "~"
                data[i][j] = "".join(the_list)
                if j < column_number - 1:
                    print(data[i][j][0: width], end=" ")
                else:
                    print(data[i][j][0: width])

# /Users/anniechen/Desktop

'''column_width = int(input())
colum_type = input().split(",")
records = []
num = len(colum_type)
while True :
    a = input()
    if a != "RECORD_END":
        b = a.split(",")
        records.append(b)
    else:
        break

#將是f的資料轉型
for a in range(len(records)):
    for b in range(len(records[a])):
        if colum_type[b] == "f":
            records[a][b] = float(records[a][b]) 


for a in range(len(records)):
    for b in range(len(records[a])):
        if type(records[a][b]) == type(" ") :
            if len(records[a][b]) <= column_width:
                if b < num-1:
                    print(f"{records[a][b]:>{column_width}s}",end=" ")
                else:
                    print(f"{records[a][b]:>{column_width}s}")  
            elif len(records[a][b]) > column_width:
                records[a][b] = records[a][b][0:column_width]
                l = list(records[a][b])
                l[column_width-1] = "~"
                records[a][b] = "".join(l)
                if b < num-1:
                    print(records[a][b][0:column_width],end=" ")
                else:
                    print(records[a][b][0:column_width])    
        elif type(records[a][b]) == type(0.0) :
            records[a][b] = str(records[a][b])
            records[a][b] = f"{float(records[a][b]):.2f}"       
            if len(records[a][b]) <= column_width:
                if b < num-1:
                    print(f"{float(records[a][b]):{column_width}.2f}",end=" ")
                else:
                    print(f"{float(records[a][b]):{column_width}.2f}")
            elif len(records[a][b]) > column_width:
                records[a][b] = records[a][b][0:column_width]
                l = list(records[a][b])
                l[column_width-1] = "~"
                records[a][b] = "".join(l)
                if b < num-1:
                    print(records[a][b][0:column_width],end=" ")
                else:
                    print(records[a][b][0:column_width])'''

#version2
# 輸入
columnWidth = int(input())
format = input().split(',')

tmp = input()
data = []
while tmp != "RECORD_END":
    tmp = tmp.split(',')
    for i in range(len(tmp)):
        # 確認資料長度或空格
        if format[i] == 'f':
            tmp[i] = '%.2f' % float(tmp[i])
        if len(tmp[i]) > columnWidth:
            tmp[i] = tmp[i][0:columnWidth-1]+'~'
        elif len(tmp[i]) < columnWidth:
            while len(tmp[i]) != columnWidth:
                tmp[i] = ' '+tmp[i]
    data.append(tmp)
    tmp = input()


for i in data:
    print(' '.join(i))
