#輸入學號
n1 = int(input())
n2 = int(input())
n3 = int(input())

#輸入科系編號
d1 = int(input())
d2 = int(input())
d3 = int(input())

#輸入保留給初選的科系編號
a1 = int(input())
a2 = int(input())

#三人科系皆不相同
if a1 == d1 :
	if a2 == d1 :
		answer = str(n1)
	elif a2 == d2 :
		answer = (str(n1) + "," + str(n2)) if (n1 < n2) else (str(n2) + "," + str(n1))
	elif a2 == d3 :
		answer = (str(n1) + "," + str(n3)) if (n1 < n3) else (str(n3) + "," + str(n1))
	else :
		answer = str(n1)
elif a1 == d2 :
	if a2 == d1 :
		answer = (str(n1) + "," + str(n2)) if (n1 < n2) else (str(n2) + "," + str(n1))
	elif a2 == d2 :
		answer = str(n2)
	elif a2 == d3 :
		answer = (str(n2) + "," + str(n3)) if (n2 < n3) else (str(n3) + "," + str(n2))
	else :
		answer = str(n2)
elif a1 == d3 :
	if a2 == d1 :
		answer = (str(n1) + "," + str(n3)) if (n1 < n3) else (str(n3) + "," + str(n1))
	elif a2 == d2 :
		answer = (str(n2) + "," + str(n3)) if (n2 < n3) else (str(n3) + "," + str(n2))
	elif a2 == d3 :
		answer = str(n3)
	else :
		answer = str(n3)
else :
	if a2 == d1 :
		answer = str(n1)
	elif a2 == d2 :
		answer = str(n2)
	elif a2 == d3 :
		answer = str(n3)
	else :
		answer = str(-1)


if a2 == d1 :
	if a1 == d1 :
		answer = str(n1)
	elif a1 == d2 :
		answer = (str(n1) + "," + str(n2)) if (n1 < n2) else (str(n2) + "," + str(n1))
	elif a1 == d3 :
		answer = (str(n1) + "," + str(n3)) if (n1 < n3) else (str(n3) + "," + str(n1))
	else :
		answer = str(n1)
elif a2 == d2 :
	if a1 == d1 :
		answer = (str(n1) + "," + str(n2)) if (n1 < n2) else (str(n2) + "," + str(n1))
	elif a1 == d2 :
		answer = str(n2)
	elif a1 == d3 :
		answer = (str(n2) + "," + str(n3)) if (n2 < n3) else (str(n3) + "," + str(n2))
	else:
		answer = str(n2)
elif a2 == d3 :
	if a1 == d1 :
		answer = (str(n1) + "," + str(n3)) if (n1 < n3) else (str(n3) + "," + str(n1))
	elif a1 == d2 :
		answer = (str(n2) + "," + str(n3)) if (n2 < n3) else (str(n3) + "," + str(n2))
	elif a1 == d3 :
		answer = str(n3)
	else :
		answer = str(n3)
else :
	if a1 == d1 :
		answer = str(n1)
	elif a1 == d2 :
		answer = str(n2)
	elif a1 == d3 :
		answer = str(n3)
	else :
		answer = str(-1)

#三人中其中兩人(d1 == d2)科系一樣
if d1 == d2 and d1 != d3 :
	if a1 == d1 == d2 :
		if a2 == d1 == d2 :
			answer = (str(n1) + "," + str(n2)) if (n1 < n2) else (str(n2) + "," + str(n1))
		elif a2 == d3 :
			if n1 < n2 < n3 :
				answer = str(n1) + "," + str(n2) + "," + str(n3)
			elif n1 < n3 < n2 : 
				answer = str(n1) + "," + str(n3) + "," + str(n2)
			elif n2 < n1 < n3 :
				answer = str(n2) + "," + str(n1) + "," + str(n3)
			elif n2 < n3 < n1 :
				answer = str(n2) + "," + str(n3) + "," + str(n1)
			elif n3 < n1 < n2 :
				answer = str(n3) + "," + str(n1) + "," + str(n2)
			else :
				answer = str(n3) + "," + str(n2) + "," + str(n1)
		else :
			answer = (str(n1) + "," + str(n2)) if (n1 < n2) else (str(n2) + "," + str(n1))
	elif a1 == d3 :
		if a2 == d1 == d2 :
			if n1 < n2 < n3 :
				answer = str(n1) + "," + str(n2) + "," + str(n3)
			elif n1 < n3 < n2 : 
				answer = str(n1) + "," + str(n3) + "," + str(n2)
			elif n2 < n1 < n3 :
				answer = str(n2) + "," + str(n1) + "," + str(n3)
			elif n2 < n3 < n1 :
				answer = str(n2) + "," + str(n3) + "," + str(n1)
			elif n3 < n1 < n2 :
				answer = str(n3) + "," + str(n1) + "," + str(n2)
			else :
				answer = str(n3) + "," + str(n2) + "," + str(n1)
		elif a2 == d3 :
			answer = str(n3)
		else :
			answer = str(n3)
	else :
		if a2 == d1 == d2 :
			answer = (str(n1) + "," + str(n2)) if (n1 < n2) else (str(n2) + "," + str(n1))
		elif a2 == d3 :
			answer = str(n3)
		else :
			answer = str(-1)

#三人中其中兩人(d2 == d3)科系一樣
if d2 == d3 and d1 != d2 :
	if a1 == d2 == d3 :
		if a2 == d2 == d3 :
			answer = str(n2) + "," + str(n3)
		elif a2 == d1 :
			if n1 < n2 < n3 :
				answer = str(n1) + "," + str(n2) + "," + str(n3)
			elif n1 < n3 < n2 : 
				answer = str(n1) + "," + str(n3) + "," + str(n2)
			elif n2 < n1 < n3 :
				answer = str(n2) + "," + str(n1) + "," + str(n3)
			elif n2 < n3 < n1 :
				answer = str(n2) + "," + str(n3) + "," + str(n1)
			elif n3 < n1 < n2 :
				answer = str(n3) + "," + str(n1) + "," + str(n2)
			else :
				answer = str(n3) + "," + str(n2) + "," + str(n1)
		else :
			answer = (str(n2) + "," + str(n3)) if (n2 < n3) else (str(n3) + "," + str(n2))
	elif a1 == d1 :
		if a2 == d2 == d3 :
			if n1 < n2 < n3 :
				answer = str(n1) + "," + str(n2) + "," + str(n3)
			elif n1 < n3 < n2 : 
				answer = str(n1) + "," + str(n3) + "," + str(n2)
			elif n2 < n1 < n3 :
				answer = str(n2) + "," + str(n1) + "," + str(n3)
			elif n2 < n3 < n1 :
				answer = str(n2) + "," + str(n3) + "," + str(n1)
			elif n3 < n1 < n2 :
				answer = str(n3) + "," + str(n1) + "," + str(n2)
			else :
				answer = str(n3) + "," + str(n2) + "," + str(n1)
		elif a2 == d1 :
			answer = str(n1)
		else :
			answer = str(n1)
	else :
		if a2 == d2 == d3 :
			answer = (str(n2) + "," + str(n3)) if (n2 < n3) else (str(n3) + "," + str(n2))
		elif a2 == d1 :
			answer = str(n1)
		else :
			answer = str(-1)

#三人中其中兩人(d1 == d3)科系一樣
if d1 == d3 and d1 != d2 :
	if a1 == d1 == d3 :
		if a2 == d1 == d3 :
			answer = str(n1) + "," + str(n3)
		elif a2 == d2 :
			if n1 < n2 < n3 :
				answer = str(n1) + "," + str(n2) + "," + str(n3)
			elif n1 < n3 < n2 : 
				answer = str(n1) + "," + str(n3) + "," + str(n2)
			elif n2 < n1 < n3 :
				answer = str(n2) + "," + str(n1) + "," + str(n3)
			elif n2 < n3 < n1 :
				answer = str(n2) + "," + str(n3) + "," + str(n1)
			elif n3 < n1 < n2 :
				answer = str(n3) + "," + str(n1) + "," + str(n2)
			else :
				answer = str(n3) + "," + str(n2) + "," + str(n1)
		else :
			answer = (str(n1) + "," + str(n3)) if (n1 < n3) else (str(n3) + "," + str(n1))
	elif a1 == d2 :
		if a2 == d1 == d3 :
			if n1 < n2 < n3 :
				answer = str(n1) + "," + str(n2) + "," + str(n3)
			elif n1 < n3 < n2 : 
				answer = str(n1) + "," + str(n3) + "," + str(n2)
			elif n2 < n1 < n3 :
				answer = str(n2) + "," + str(n1) + "," + str(n3)
			elif n2 < n3 < n1 :
				answer = str(n2) + "," + str(n3) + "," + str(n1)
			elif n3 < n1 < n2 :
				answer = str(n3) + "," + str(n1) + "," + str(n2)
			else :
				answer = str(n3) + "," + str(n2) + "," + str(n1)
		elif a2 == d2 :
			answer = str(n2)
		else :
			answer = str(n2)
	else :
		if a2 == d1 == d3 :
			answer = (str(n1) + "," + str(n3)) if (n1 < n3) else (str(n3) + "," + str(n1))
		elif a2 == d2 :
			answer = str(n2)
		else :
			answer = str(-1)

#三人科系一樣
if d1 == d2 == d3 :
	if (a1 == d1 == d2 == d3) or (a2 == d1 == d2 == d3) :
		if n1 < n2 < n3 :
			answer = str(n1) + "," + str(n2) + "," + str(n3)
		elif n1 < n3 < n2 : 
			answer = str(n1) + "," + str(n3) + "," + str(n2)
		elif n2 < n1 < n3 :
			answer = str(n2) + "," + str(n1) + "," + str(n3)
		elif n2 < n3 < n1 :
			answer = str(n2) + "," + str(n3) + "," + str(n1)
		elif n3 < n1 < n2 :
			answer = str(n3) + "," + str(n1) + "," + str(n2)
		else :
			answer = str(n3) + "," + str(n2) + "," + str(n1)
	else :
		answer = str(-1)
print(answer)