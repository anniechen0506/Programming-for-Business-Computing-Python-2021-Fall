x1 = int(input())
x2 = int(input())
x3 = int(input())
p = int(input())

money = x1 + (5 * x2) + (10 * x3)
rest = 0

if money >= 100 :
	rest = money - p 
else :
	rest = money

print(rest)
