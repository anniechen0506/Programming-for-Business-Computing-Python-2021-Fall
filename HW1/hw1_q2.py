x1 = int(input())
x2 = int(input())
r = int(input())
y = int(input())

if y <= x1 :
	answer = str(x1-y) + "," + str(x2+r*y)
else :
	answer = str(x1-x1) + "," + str(x2+r*x1)

print(answer)