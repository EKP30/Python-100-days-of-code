print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction_choice = input("You are in an alleyway with one path leading left and the other right. Right or left...\n")
direction_choice.lower()
if direction_choice == "right":
  print("Someone can tell you are from California and you get shot. Game over.")
elif direction_choice == "left":
  swim_stay = input("You safely arrive at a river. Do you choose to swim or stay?\n")
  swim_stay.lower()
if swim_stay == "swim":
  print("You are swimming across when you get caught on someone's fishing line and die from the bleeding. If you couldn't tell, game over.")
elif swim_stay == "stay":
  red_blue_yellow = input("It takes a while, but a boat with a California sticker shows up and gives you a ride. After you get across the river, you walk into an old abandoned house that has a red door, a blue door, and a yellow door. Type 'red' 'blue' or 'yellow' for your choice.\n")
red_blue_yellow.lower()
str(red_blue_yellow)
if red_blue_yellow == "red":
  print("You walk into a room full of deadly, poisonous snakes and die. Obviously game over.")
elif red_blue_yellow == "yellow":
  print("You walk into a room full of starvationing tigers and are eaten alive. WOW! How did you know it is game over!")
elif red_blue_yellow == "blue":
  print("You walk into the blue door very cautiously, expecting something terrible or something amazing. You see the treasure and start acting like a 12-year-old boy after his first few 6-8 hour work days without any breaks. You are briefly reminded of someone after reading this but then completely forget when you remember about the treasure. Cogratulations, you won!")
