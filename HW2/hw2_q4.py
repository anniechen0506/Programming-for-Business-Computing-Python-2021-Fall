n = int(input()) #order_total 訂單總數
t = int(input()) #unit_price_threshold 單價門檻
q1 = int(input()) #employee 1 working time 員工一工作時間
q2 = int(input()) #employee 2 working time 員工二工作時間
remain_time_1 = 480
remain_time_2 = 480
unit_price = 0
accept = 0

for i in range(n+1) :
	x = int(input()) #total number of toy car 玩具車數量
	p = int(input()) #total value of the order 該訂單總價
	unit_price = p / x
	remain_time_1 = remain_time_1 - (q1 * x)
	remain_time_2 = remain_time_2 - (q2 * x)

	if (unit_price >= t) and (remain_time_1 >= 0) and (remain_time_2 >= 0) :
		accept = i
		print(accept)
	else :
		continue
