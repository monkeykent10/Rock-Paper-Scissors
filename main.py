import random

games_played = 0
user_wins = 0
quit = "no"

def user_option():
    user_choice = input("\nChoose Rock, Paper, or Scissors: ")
    if user_choice in ["Rock", "rock", "R", "r"]:
        user_choice = "Rock"

    elif user_choice in ["Paper", "paper", "P", "p"]:
        user_choice = "Paper"

    elif user_choice in ["Scissors", "Scissor", "scissors", "scissor", "S", "s"]:
        user_choice = "Scissors"

    else:
        print("\nI did not understand that. Please try again. ")
        pass
        # user_option()
    return user_choice


def comp_option():
    comp_choice = random.randint(0, 2)
    if comp_choice == 0:
        comp_choice = "Rock"
    elif comp_choice == 1:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    return comp_choice


while quit == "no":
    #Describes the rules of the game and takes user input to either end game or keep playing
    comp_choice = comp_option()
    user_choice = user_option()

    if comp_choice == "Rock":
        if user_choice == "Rock":
            print("You both chose rock. It was a tie.")
            games_played += 1
        elif user_choice == "Paper":
            print("Your paper beat their rock. You won!")
            games_played += 1
            user_wins += 1
        elif user_choice == "Scissors":
            print("Your scissors lost to their rock. You lost.")
            games_played += 1

    elif comp_choice == "Paper":
        if user_choice == "Paper":
            print("You both chose paper. It was a tie.")
            games_played += 1
        elif user_choice == "Rock":
            print("Your rock lost to their paper. You lost.")
            games_played += 1
        elif user_choice == "Scissors":
            print("Your scissors beat their paper. You won!")
            games_played += 1
            user_wins += 1

    elif comp_choice == "Scissors":
        if user_choice == "Scissors":
            print("You both chose scissors. It was a tie.")
            games_played += 1
        elif user_choice == "Rock":
            print("Your rock beat their scissors. You won!")
            games_played += 1
            user_wins += 1
        elif user_choice == "Paper":
            print("Your paper lost to their scissors. You lost.")
            games_played += 1

    user_choice = input("\nDo you want to keep playing? If so, type yes: ")
    if user_choice in ["Yes", "yes", "Y", "y"]:
        pass
    else:
        print("\nGames played: " + str(games_played))
        print("Games won: " + str(user_wins))
        quit = "yes"