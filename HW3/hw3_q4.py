n_B_list = input().split(',')
w_list = input().split(',')
v_list = input().split(',')
k = int(input())
total_weight = 0
total_value = 0
best_method = 1000

for i in range(len(n_B_list)):
	n_B_list[i] = int(n_B_list[i])
	n = n_B_list[0]
	B = n_B_list[1]
for i in range(len(w_list)):
	w_list[i] = int(w_list[i])
for i in range(len(v_list)):
	v_list[i] = int(v_list[i])

for i in range(1, k+1):
	x_list = input().split(',')
	for x in range(len(x_list)):
		x_list[x] = int(x_list[x])
	for a in range(len(w_list)):
		weight = 0
		value = 0
		for b in range(a+1):
			weight += (w_list[b])*(x_list[b+1])
			value += (v_list[b])*(x_list[b+1])
	if (weight <= B) and (value > total_value):
		total_weight = weight
		total_value = value
		best_method = x_list[0]
	elif (weight <= B) and (value == total_value):
		if x_list[0] < best_method:
			total_weight = weight
			total_value = value
			best_method = x_list[0]

print(str(best_method) + "," + str(total_weight) + "," + str(total_value))
