town_firestation_list = input().split(',') # town number and fire station number 城鎮數量以及消防局預計數量
town_num = int(town_firestation_list[0])
firestation_num = int(town_firestation_list[1])

predict_fire_list = input().split(',') # predicted fire happened time 各個城鎮預期失火次數
for i in range(len(predict_fire_list)):
	predict_fire_list[i] = int(predict_fire_list[i]) 

dis_list = []
firestation_town = []
no_firestation_town = []

for x in range(town_num):
	dis = input().split(',')
	dis_list.append(dis)
	no_firestation_town.append(x)

first_station_min_distance = 100000000000
first_station = 0

for i in range(town_num):
	total_distance = 0
	for j in range(town_num):
		total_distance += int(dis_list[i][j]) * int(predict_fire_list[j])

	if total_distance < first_station_min_distance:
		first_station_min_distance = total_distance
		first_station = i
	elif total_distance == first_station_min_distance:
		if i < first_station:
			first_station_min_distance = total_distance
			first_station = i
		else:
			continue
	else:
		continue

# find the first town to build fire station 找到第一個蓋消防局的城鎮
#print(str(first_station) + "," + str(first_station_min_distance))

firestation_town.append(first_station)
no_firestation_town.remove(first_station)

if firestation_num > 1:
	for m in range(firestation_num - 1):
		next_firestation = 0
		max_dis = -10000000
		for r in no_firestation_town:
			min_dis = 100000000
			for s in firestation_town: #跟有消防局的城鎮的距離
				if int(dis_list[r][s]) < min_dis:
					min_dis = int(dis_list[r][s])
				else:
					continue
			if min_dis > max_dis:
				max_dis = min_dis
				next_firestation = r
			elif min_dis == max_dis:
				if r < next_firestation:
					next_firestation = r
					max_dis = min_dis 

		firestation_town.append(next_firestation)
		no_firestation_town.remove(next_firestation)

final_distance = 0
for p in no_firestation_town:
	min_final_dis = 1000000000
	for q in firestation_town:
		if int(dis_list[p][q]) < int(min_final_dis):
			min_final_dis = dis_list[p][q]

	final_distance += int(min_final_dis) * int(predict_fire_list[p])

for k in range(len(firestation_town)):
	firestation_town[k] = firestation_town[k] + 1

if len(firestation_town) >= 2:
	for t in range(len(firestation_town)-1):
		print(str(firestation_town[t]), end = ",")
	print(str(firestation_town[-1]) + ";" + str (final_distance))
else:
	print(str(firestation_town[0]) + ";" + str(final_distance))
