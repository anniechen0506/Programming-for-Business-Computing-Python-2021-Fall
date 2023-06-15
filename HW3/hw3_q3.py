n,B = input().split(',')
B = int(B)
total_weight = 0
total_value = 0
w_list = input().split(',')
v_list = input().split(',')
x_list = input().split(',')

for i in range(len(x_list)) :
	x_list[i] = int(x_list[i])
for i in range(len(w_list)) :
	w_list[i] = int(w_list[i])
for i in range(len(v_list)) :
	v_list[i] = int(v_list[i])

for i in range(len(x_list)) :
	if x_list[i] == 1 :
		total_weight += w_list[i]
		total_value += v_list[i]
	else :
		continue

if total_weight > B :
	print(str(-1))
else :
	print(str(total_weight) + "," + str(total_value))
