prompt = '\nPlease tell me your Age:'

while True:
	age = int(raw_input(prompt))
	
	if age < 3:
		print("hi, my kid's, you free" )
		continue
	elif 3 <= age < 12:
		print("10 $")
		continue
	elif age >= 12:
		print("15 $")
		continue
