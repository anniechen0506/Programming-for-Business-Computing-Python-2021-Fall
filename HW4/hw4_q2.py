town_num = int(input()) #城鎮數量
fire_num_list = input().split(',') #各個城鎮預期失火次數
min_dis = 10000000000
best_town = 0

for i in range(len(fire_num_list)):
	fire_num_list[i] = int(fire_num_list[i]) 

for i in range(1, town_num+1):
	dis_list = input().split(',')
	for x in range(len(dis_list)):
		dis_list[x] = int(dis_list[x])
	for a in range(len(dis_list)):
		total_dis = 0
		for b in range(a+1):
			total_dis += (fire_num_list[b] * (dis_list[b]))
	if total_dis < min_dis:
		min_dis = total_dis
		best_town = i
	elif total_dis == min_dis:
		if i < best_town:
			best_town = i
		else:
			continue
	else:
		continue

print(str(best_town) + "," + str(min_dis))
