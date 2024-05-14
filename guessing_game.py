import random

#Lists to be used for statistics of guesses later on
#user_num_guesses = []
#comp_num_guesses = []

#Function to check that user input is int and within range of computer guesses. 
#Returns appropriate message to guide player to the number and success message when correct.
def user_guess(num,comp):
    while True:
        if not type(num) is int or num not in range(0,10):
            num = int(input("Only type integers between zero (0) and nine (9). Please try again.\n"))
            continue
        elif num > comp:
            #command to add user guess to its appropriate list.
            #user_num_guesses.append(num)
            num = int(input("Too high. Try again.\n"))
        elif num < comp:
            #command to add user guess to its appropriate list.
            #user_num_guesses.append(num)
            num = int(input("Too low. Try again.\n"))
        elif num == comp:
            #command to add user guess to its appropriate list.
            #user_num_guesses.append(num)
            print("Correct!")
            break
            
#Gathers user desire to play guessing game.
game_status = int(input("Would you like to play a guessing game?\nThe computer will pick a random number between zero (0) and nine (9).\nYour goal is to choose the same number.\n1 - Yes\n2 - No\n"))

#Loop to make game run continously until user indicates otherwise. 
while True:
    try:
        #Checks user input to ensure it is either 1 or 2. 
        if game_status not in (1,2):
            raise ValueError
        #Exit game is user indicates they do not wish to play. 
        elif game_status == 2:
            break
        #Initiates guessing game after play indicates desire to play.
        #Starts with random computer seleciton of a number 0 through 9 and inserts into vartiable. 
        elif game_status == 1:
            num_rand = random.randint(0,9)
            #Below adds computer selection to the appropriate list. 
            #comp_num_guesses.append(num_rand)
            user_num = int(input(("The computer has selected a random number between zero (0) and nine (9).\nPlease enter the number you'd like to guess.\n")))
            #Runs function to pit user entry to computer selection.
            user_guess(user_num, num_rand)
            #Gathers user desire to continue playing. 
            game_status = int(input("Would you like to play again?\n1 - Yes\n2 - No\n"))
    #Universal error message if user enter improper input.         
    except ValueError:
        game_status = int(input("Please only type 1 or 2 to indicate whether or not you'd like to play.\n1 - Yes\n2 - No\n"))


#Upcoming additions:
    #Statistics histograms of computer choices and user guesses.
    #Accuracy measures.

    


    

    

