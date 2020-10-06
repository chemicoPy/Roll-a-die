import sys
import random


roll = input("Enter 'roll me' to roll the dice:").lower()
dice =  random.randint(1,6)


def back():
    back = input("Would you like to roll the dice again?. (Yes or No) ").lower()
    
    if back == 'yes':
        print('You got', random.randint(1,6), 'this time around.')
             
    elif back =='no':
        sys.exit()
    
    else:
       print('Follow the instructions!. Now you do not have choice but to start all over.')
       sys.exit()
          
    return
            
    
while roll == 'roll me':
    print(dice)
    
    if dice == 6:
        print('Wow, you got a', dice,'!.')
    
    break
    

else:
    print("Invalid input!. Enter 'roll me' to roll the dice ")

back()


        













