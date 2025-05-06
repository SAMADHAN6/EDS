#target 3: build an automatic pizza order program.

print("Hello! Welcome to Python Pizza Deliveries!")
print("**********************************************")
size=input("What size pizza do you want?S,M or L: ")
if (size.upper() == "S"):
	bill=15;
elif (size.upper() == "M"):
	bill=20
elif (size.upper() == "L"):
	bill=25
else:
	print("Wrong input")
pepperoni=input("Do you want pepperoni on your pizza? Y or N: ")
if( pepperoni.upper() == "Y" and (size.upper()=="M" or size.upper() == "L")):
	bill+=3
elif (pepperoni.upper() == "Y" and size.upper()=="S"):
	bill+=2
elif (pepperoni.upper()=="N"):
	pass
else:
	print("Wrong Input!")

extra_cheese=input("Do you want extra cheese? Y or N: ")
if(extra_cheese.upper() == "Y"):
	bill+=1
elif (extra_cheese.upper()=="N"):
	pass
else:
	print("Wrong Input")

print("**********************************************")
print(f"Your final bill is: ${bill} ")

