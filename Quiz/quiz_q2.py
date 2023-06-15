n,t,q = input().split(',')
n = int(n)
t = int(t)
q = int(q)
p_list = input().split(',')
x_list = input().split(',')
money = 0 #金額總數
rest = 0 #是否買了葡萄柚綠茶之後
hundred = 0 #媽媽要拿走幾百
mom = 0 #媽媽拿走的 
take = 0 #給媽媽之後剩下的

for i in range(len(p_list)) :
	p_list[i] = int(p_list[i])
	x_list[i] = int(x_list[i])
	money = money + (p_list[i] * x_list[i])

if (money >= t) and (money >= q) :
	rest = money - q
else :
	rest = money

if rest >= 100 :
	hundred = rest // 100
	mom = hundred * 100
	take = rest - mom
else :
	take = rest

print(str(take) + "," + str(mom))
