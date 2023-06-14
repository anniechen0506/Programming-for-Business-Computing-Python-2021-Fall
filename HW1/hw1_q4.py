x = int(input())
y = int(input())

#取x的每位數
x_hundreds = int(x // 100)
x_tens = int((x % 100) // 10)
x_units = int(x % 10)

#取y的每位數
y_hundreds = int(y // 100)
y_tens = int((y % 100) // 10)
y_units = int(y % 10)

if x == y : #3A
	answer = str("3A0B")
else : #2A
	if (x_hundreds == y_hundreds) and (x_tens == y_tens) and (x_units != y_units) :
		answer = str("2A0B")
	elif (x_hundreds == y_hundreds) and (x_tens != y_tens) and (x_units == y_units) :
		answer = str("2A0B")
	elif (x_hundreds != y_hundreds) and (x_tens == y_tens) and (x_units == y_units) :
		answer = str("2A0B")
	else : #1A
		if (x_hundreds == y_hundreds) and (x_tens != y_tens) and (x_units != y_units) :
			if (x_tens == y_units) and (x_units == y_tens) :
				answer = str("1A2B")
			elif (x_tens == y_units) and (x_units != y_tens) :
				answer = str("1A1B")
			elif (x_tens != y_units) and (x_units == y_tens) :
				answer = str("1A1B")
			else :
				answer = str("1A0B")
		elif (x_hundreds != y_hundreds) and (x_tens == y_tens) and (x_units != y_units) :
			if (x_hundreds == y_units) and (x_units == y_hundreds) :
				answer = str("1A2B")
			elif (x_hundreds == y_units) and (x_units != y_hundreds) :
				answer = str("1A1B")
			elif (x_hundreds != y_units) and (x_units == y_hundreds) :
				answer = str("1A1B")
			else :
				answer = str("1A0B")
		elif (x_hundreds != y_hundreds) and (x_tens != y_tens) and (x_units == y_units) :
			if (x_hundreds == y_tens) and (x_tens == y_hundreds) :
				answer = str("1A2B")
			elif (x_hundreds == y_tens) and (x_tens != y_hundreds) :
				answer = str("1A1B")
			elif (x_hundreds != y_tens) and (x_tens == y_hundreds) :
				answer = str("1A1B")
			else :
				answer = str("1A0B")
		else : #0A
			if (x_hundreds != y_hundreds) and (x_tens != y_tens) and (x_units != y_units) :
				if (x_hundreds == y_tens) and (x_tens == y_units) and (x_units == y_hundreds) :
					answer = str("0A3B")
				elif (x_hundreds == y_units) and (x_tens == y_hundreds) and (x_units == y_tens) :
					answer = str("0A3B")
				elif (x_hundreds != y_hundreds) and (x_tens == y_units) and (x_units == y_tens) :
					answer = str("0A2B")
				elif (x_tens != y_tens) and (x_hundreds == y_units) and (x_units == y_hundreds) :
					answer = str("0A2B")
				elif (x_units != y_units) and (x_hundreds == y_tens) and (x_tens == y_hundreds) :
					answer = str("0A2B")
				else :
					if (x_hundreds == y_tens) and (x_tens != y_hundreds) and (x_tens != y_units) and (x_units != y_hundreds) and (x_units != y_units) :
						answer = str("0A1B")
					elif (x_hundreds == y_units) and (x_tens != y_hundreds) and (x_tens != y_tens) and (x_units != y_hundreds) and (x_units != y_tens) :
						answer = str("0A1B")
					elif (x_tens == y_hundreds) and (x_hundreds != y_tens) and (x_hundreds != y_units) and (x_units != y_tens) and (x_units != y_units) :
						answer = str("0A1B")
					elif (x_tens == y_units) and (x_hundreds != y_hundreds) and (x_hundreds != y_tens) and (x_units != y_hundreds) and (x_units != y_tens) :
						answer = str("0A1B")
					elif (x_units == y_hundreds) and (x_hundreds != y_tens) and (x_hundreds != y_units) and (x_tens != y_tens) and (x_tens != y_units) :
						answer = str("0A1B")
					elif (x_units == y_tens) and (x_hundreds != y_hundreds) and (x_hundreds != y_units) and (x_tens != y_hundreds) and (x_tens != y_units) :
						answer = str("0A1B")
					else :
						answer = str("0A0B")
print(answer)
