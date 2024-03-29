import random

#Dictionary for game choices.
game_options = {
    1:"Rock", 
    2:"Paper", 
    3:"Scissors"
    }

#Variables for record counter.
user_wins = 0
computer_wins = 0
ties = 0

#Function to run the game. Takes in user choice and randomized house(computer) choice.
def game(user, house):
    global user_wins, computer_wins, ties
    print("User chose " + str(game_options.get(user))) #Verifies user choice from input below. Gathers value from game_options dict. 
    print("House chose " + str(game_options.get(house))) #Presents randomized house/computer choice.

    #if/elif block to compare choices for all cases and print win or loss message accordingly. Increments appropriate record field. 
    if user == house:
        print("Tie")
        ties += 1
    elif user == 1 and house == 3:
        print("You win! Rock beats Scissors")
        user_wins += 1
    elif user == 1 and house == 2:
        print("Sorry, you lost. Paper covers rock.")
        computer_wins += 1
    elif user == 2 and house == 1:
        print("You win! Paper covers rock.")
        user_wins += 1
    elif user == 2 and house == 3:
        print("Sorry, you lost. Scissors cut paper.")
        computer_wins += 1
    elif user == 3 and house == 1:
        print("Sorry, you lost. Rock beats Scissors")
        computer_wins += 1
    elif user == 3 and house == 2:
        print("You win! Scissors cut paper.")
        user_wins += 1

#Default selection to have the game run.
while True:
    game_status = int(input("Would you like to play rock, paper, scissors?\n1 - Yes\n2 - No\n")) #Initial selection on if the user would like to play. 
    if game_status in [1, 2]:
        break
    print("Please indicate using 1 or 2 if you'd like to play.")

#While loop to run the game function while user indicates they'd like to play.
while game_status == 1 :
    #Nested while loops in place as error catches if user does not provide appropriate input.    
    while True:
        user = int(input("Type:\n1 - Rock\n2 - Paper\n3 - Scissors\n")) #Gathers user choice as integer. 
        if user in game_options.keys():
            break
        print("Please only enter 1, 2, or 3 for your selection.")
    house = random.choice(list(game_options.keys())) #Gathers random choice from game_options dict. Only gets 1 - 3 key, but will print associated value in-game. 
    game(user, house) #Compares choices to determine the winner. Print statements indicating user win/loss are provided by the game function.
    print("Record:\nUser wins: " + str(user_wins) + "\nComputer wins: " + str(computer_wins) + "\nTies: " + str(ties)) #Displays current session record of user wins, computer wins, and ties.
    while True:
        game_status = int(input("Would you like to play again?\n1 - Yes\n2 - No\n")) #Asks user if they'd like to continue. Record will continue over from previous games. If not, record will not save.
        if game_status in [1, 2]:
            break
        print("Please indicate using 1 or 2 if you'd like to play.")