# RPG game element - Aaron Fuata

#Import libraries 
import time
import random
from colorama import Fore, Back, Style

#List of greetings, leaving, & hero inventory
greetings = ["Howdy partner!", "Bonjourrr!", "Greetings friend!", "Kia Ora!"]
leaving = ["Adios amigo!", "Goodbye my friend!", "Later bo!", "Till we meet again!"]
hero_inventory = ["Healing potion", "Red gem", "Sword", "Armour"]

#Speak function
def speak(text):
    print(Fore.GREEN + Style.BRIGHT + text + Style.RESET_ALL)

#Guess my number function
def guess_my_number(item):
    speak("Game on! The game is guess my number.")
    
    #Random.randint to randomly pick number
    number = random.randint(1, 10)

    #While loop for the guess my number game
    while True:
        #Handles unexpected/expected input
        try:
            attempt = int(input("I'm thinking of a number between 1 & 10, guess: "))
            break
        except ValueError:
            speak("Error, please input a number!")
    
    
    if attempt == number:
        speak("Good job, you got it!")
    else:
        speak("Incorrect! The number {}.".format(number)) #.format formats the desired value and inserts it inside the string
        
        if item in hero_inventory:
            hero_inventory.remove(item)
            speak("Sucks to be you! You just lost your {}".format(item))
        else:
            speak("This item is not in your inventory!")
            
print("") #Gives space so the console is easier to read
speak("A money hungry goblin approaches you!")

#Options for the user
while True:
    speak("Select an option to continue:")
    speak("1 - Greet the goblin")
    speak("2 - Play a game")
    speak("3 - Say farewell")
    
    user_choice = input("""Enter your decision here(1-3)
>> """)
    
    if user_choice == "1":
        print("")   
        speak(random.choice(greetings)) #random.choice in this case randomly picks a greeting from its list
        
    elif user_choice == "2":
        print("")   
        if len(hero_inventory) == 0: #Checks if length of hero inventory is 0(no items) if is 0 enters if block
            speak("There are currently no items in your inventory!")
        else:
            print("")   
            speak("Pick an item from your inventory that you're willing to bet on!")
            index = 1 #initilised to 1 - iterate over inventory items
            while index <= len(hero_inventory): #continues until index is greater than hero inventory length
                item = hero_inventory[index - 1]
                speak("{}: {}".format(index, item))
                index += 1
                
            while True:
                try:
                    user_item = int(input("Enter number of item: "))
                    print("")   
                    if 1 <= user_item <= len(hero_inventory):
                        player_item = hero_inventory[user_item - 1]
                        guess_my_number(player_item)
                        break
                    else:
                        print("")   
                        speak("Error, please enter a valid item number!")
                except ValueError:
                    print("")   
                    speak("Error, please enter a number")
    #option 3 of code which simply exits the program with a random choice from 'leaving' string              
    elif user_choice == "3":
        print("")   
        speak(random.choice(leaving))
        break
    
    else:
        speak("Error! Please select a number(1-3)!")

