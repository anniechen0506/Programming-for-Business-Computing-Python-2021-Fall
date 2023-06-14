n = int(input())
x = int(input())
y = int(input())
r = int(input())

if r >= n :
	answer = n * x + (r - n) * y
else :
	answer = r * x

print(answer)
