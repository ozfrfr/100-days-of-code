print('''
       _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
      ''')

print(r''' 
                 ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/             /
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
        ''')

print('''                   
                    Welcome to Treasure Island
               Your mission is to find the treasure.
        ''')

enter = input('Type "Enter" to start the game \n \n')

enter_lowercase = enter.lower()

if enter_lowercase == "enter":

    print('''
            You\'re at a crossroad, where do you go?
                    ''')
    left_or_right = input('Type "Left" or "Right"? \n \n')
    left_or_right_lowercase = left_or_right.lower()

    if left_or_right_lowercase == "right":
        print('''                   
                    You fell into a hole.
                        Game Over.
                        ''')

    elif left_or_right_lowercase != "right" and left_or_right_lowercase != "left":
        print('''
                    You entered an invalid direction.
                                Game Over.
                        ''')

    elif left_or_right_lowercase == "left": 
        print('''
            You\'ve come to a lake. There is an island in the middle of the lake.
                        ''')
        swim_or_wait = input('Type "Wait" to wait for a boat or type "Swim" to swim across. \n \n')
        swim_or_wait_lowercase = swim_or_wait.lower()
    
        if swim_or_wait_lowercase == "swim":
            print('''                
                    You got eaten crocodiles. 
                            Game Over.
                            ''')
        elif swim_or_wait_lowercase != "swim" and swim_or_wait_lowercase != "wait" :
            print('''
                    You entered the an invalid decision.
                                Game Over.
                            ''')
    
        elif swim_or_wait_lowercase == "wait":
            print('''
                You have arrived at the Island unharmed. 
                There is a house with 3 doors,
                one Red, one Yellow and one Blue. 
                            ''') 
            which_door = input('Choose a door, Type  "Blue", "Yellow" or "Red"? \n \n')
            which_door_lowercase = which_door.lower()
            
            if which_door_lowercase == "red":
                print('''   
                    Its a room full of fire.
                            Game Over.
                        ''')
            elif which_door_lowercase == "blue":
                print('''   
                    Its a room full of beasts.
                            Game Over.
                        ''')
            elif which_door_lowercase == "yellow":
                print('''       
        sAy YelLoOWw!                               YelLoOWw!!
                        You Found The Treasure!
                                You Win!
        sAy YelLoOWw!                               YelLoOWw!!
                        ''')
            else:
                print('''
                    You entered an invalid door.
                            Game Over.
                        ''')

