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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
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

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

step1 = input(
    "\nYou enter a dark cave and can only go left or right, which way will you go?\nL or R: ").lower()

if step1 == "l" or step1 == "left":
    step2 = input("\n\nThe tunnel seems to go on forever but, you hear a loud bang and running water. Suddenly, you have wet feet and realise you're standing at the edge of a large underground lake. What do you do? \nSwim or Wait?: ").lower()

    if step2 == "wait" or step2 == "w":
        step3 = input("\n\nYou feel the water with your hand and realise the lake is getting smaller so decide to wait. When the lake has drained, you notice a sink hole had appeared and sucked away the water - good call! It takes you a while to cross the lake but, you eventually arrive at the other side where you see 3 door: one red, one green and one blue. Which door do you choose or, do you head back?\nR, B, G or Back:").lower()

        if step3 == "back" or step3 == "go back":
            print("\n\nOn second thoughts, this treasure really isn't worth the risk! You head back the way you came as it's just a straight line, avoiding the sink hole and eventually turning right out of the tunnel and into the sunlight. Outside there is a stranger who laughs and tells you that the whole thing was a pointless test that you passed and gave you a voucher for a year's worth of stale Starbucks sandwiches - wow, it really was pointless but, at least you survived!")
        elif step3 == "r" or step3 == "red":
            print("\n\nYou open the red door and step inside it's very warm but, everything looks fine and you head towards what seems like the exit. As you try to open it, the door you came in from slams shut and you hear an evil laugh. Suddenly the floor starts to retract into the wall and below you is a pit of lava. You have nowhere to go, the doors are locked tight and eventually you run out of floor\n\nGAME OVER")
        elif step3 == "g" or step3 == "green":
            print("\n\nYou open the gree door and step inside it's full of plants and smells great! You see a chest in the middle of the room and go towards it. You gently try to open the chest and to your surprise, it's unlocked! As you open it, you soon dicover it is boobytrapped and acid sprays into your eyes blinding you. You hear a door slam shut, an evil laugh and realise, you are trapped and helpless. You eventually die and become nutrition for the plants of the room\n\nGAME OVER")
        elif step3 == "b" or step3 == "blue":
            print("\n\nYou open the blue door and see a chest in the centre of the room. You go to open it and suddenly, the door behind you slams shut. There is an evil laugh and the room begins to slowly flood with water. You realise there is no way out and accept your fate while thinking that maybe being sucked into that lake sinkhole would have been a faster death as it's going to take forever to fill the room. You eventually drowned... finally!\n\nGAME OVER")
        else:
            print('''\n\n"You thought you were smart!" says a random voice. The echoes of the cave make it impossible to pinpoint the direction it\'s coming from. "Now for your reward..." it continues and you suddenly feel a sharp pain in your shoulder. You've been hit with a poison dart and begin to lose consciouness before dying\n\nGAME OVER''')

    elif step2 == "swim" or step2 == "s":
        print("\n\nYou're a confident swimmer and you see no danger so, begin to swim across. However, you were unaware of the strong current and suddenly realise the lake is draining and you can't fight it. You're sucked into the vortex created by a sink hole and perish\n\nGAME OVER")
    else:
        print("\n\nYou had TWO choices but, you decided to make up a 3rd one, and for that, I've gone and emptied your bank account and killed your character! Oh, they died in some really boring way but, you're now poor so, good luck!\n\nGAME OVER")

elif step1 == "r" or step1 == "right":
    print("\n\nIt was dark and you couldn't see where you were going. You fell into a really deep hole and broke both your legs. Unfortunately, no-one came in time to save you and died of dehydration.\n\nGAME OVER")
else:
    print("\n\nReally!? Because you couldn't follow basic instructions, you slowly and painful start to implode. It takes about 5 minutes for you to die and the whole time you think to yourself that trying to be smart really was not worth it!\n\nGAME OVER")
