#Target 4: Treasure Hunt

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to the Treasure Hunt!!")
choice=input("Enter S to start: ")
if (choice.upper() == "S"):
    print("**********************************************")
    print("There's a turn ahead!! Choose wisely")
    ch1=input("Enter L to turn left and R to turn right: ")
    if (ch1.upper()== "R"):
        print("There's another turn ahead!! Choose wisely")
        ch2=input("Enter L to turn left and R to turn right: ")
        if(ch2.upper() == "R"):
            print("There's another turn ahead!! Choose wisely")
            ch3=input("Enter L to turn left and R to turn right: ")
            if(ch3.upper()=="L"):
                print("Well Done!! Now you can see three houses in front of you House 1 , House 2 and House 3")
                ch4=int(input("Enter 1 to enter House 1, 2 to enter House 2 and 3 to enter House 3: "))
                if(ch4 == 1):
                    print("GAME OVER!!")
                elif (ch4 == 2):
                    print("Congratulations! You've completed the Treasure Hunt.")
                elif (ch4 == 3):
                    print("GAME OVER!!")
            else:
                print("GAME OVER!!")
        else:
                print("GAME OVER!!")

    else:
                print("GAME OVER!!")






