#If the number given by the user is even or odd
a=int(input("Enter any number:"))
if (a%2==0 and a!=0):
	print("Number is even")
elif a==0:
	print("Number is 0")
else:
	print("Number is odd")