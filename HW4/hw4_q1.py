temp = input().split(',')
for i in range(len(temp)):
	temp[i] = int(temp[i])
n = temp[0] #n種面額
m = temp[1] #m種食材

coin_list = input().split(',')
coin_num_list = input().split(',')
food_list = input().split(',')

for i in range(len(coin_list)):
	coin_list[i] = int(coin_list[i])
	coin_num_list[i] = int(coin_num_list[i])
for j in range(len(food_list)):
	food_list[j] = int(food_list[j])

total_money = 0

for i in range(len(coin_list)):
	total_money += coin_list[i] * coin_num_list[i]

for j in range(len(food_list)):
	if food_list[j] <= total_money:
		total_money = total_money - food_list[j]
	else:
		continue

print(total_money)
