unit = input("Please enter the unit you want to convert to? (C/F): ") #想轉換成的單位

if unit == "C":
	tempreture = input("Please enter the tempreture in Fahrenheit: ")
	tempreture = float(tempreture)
	tempreture_C = (tempreture - 32) * 5/9
	print(tempreture, "F =", tempreture_C, "C")

if unit == "F":
	tempreture = input("Please enter the tempreture in Celsius: ")
	tempreture = float(tempreture)
	tempreture_F = tempreture * 9/5 + 32
	print(tempreture, "C =", tempreture_F, "F")
