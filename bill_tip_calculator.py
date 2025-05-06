#Target 2: Bill calculator
bill=float(input("Enter the bill: "))
num_of_people=int(input("Enter the number of people: "))
tip=int(input("Enter the tip: "))
bill_per_person= (bill/num_of_people) + ((12/100)*(bill/num_of_people))
print("Each person should pay:", round(bill_per_person,2))