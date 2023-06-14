method_num = int(input()) #包裝方法數
a = 0
b = 0
c = 0
price = 0 
optimal_price = 0
profit = 0
max_profit = 0
optimal_method = 0

for i in range(1, method_num + 1) :
	a = int(input())
	b = int(input())
	c = int(input())
	for p in range(c, a // b + 1) :
		price = p
		profit = (a - b * p) * (p - c)

		if (profit > max_profit) :
			max_profit = profit
			optimal_price = price
			optimal_method = i
		elif (profit == max_profit) :
			if optimal_method == i :
				optimal_price = price
		else :
			continue

	if (max_profit <= 0) :
		optimal_method = 1
		optimal_price = 1000

print(str(optimal_method) + "," + str(optimal_price) + "," + str(max_profit))
