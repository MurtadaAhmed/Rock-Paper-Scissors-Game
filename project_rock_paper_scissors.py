import random  # to generate a random computer move
from colorama import Fore, Back, Style  # to color the printed text
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Write [r] for Rock, [p] for Paper, [s] for Scissors or [e] to exit: ")
while player_move != "e":

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:  # if the input is invalid
        raise SystemExit("Invalid Input. Please try again (you need to enter [r], [p] or [s]).")

    computer_move = ""  # where we gonna store the computer move
    computer_random_number = random.randint(1, 3)  # the computer will choose a number between 1 and 3 inclusive
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    # now we will compare player_move and computer_move to decide who wins
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(Fore.YELLOW +f"The computer chose {computer_move}")
        print(Fore.GREEN + "You win!")
    elif player_move == computer_move:
        print(Fore.YELLOW + f"The computer chose {computer_move}")
        print(Fore.BLUE + "Draw!")
    else:
        print(Fore.YELLOW + f"The computer chose {computer_move}")
        print(Fore.RED + "You lost!")
    print(Style.RESET_ALL)  # to reset the color for the next loop
    player_move = input("Write [r] for Rock, [p] for Paper, [s] for Scissors or [e] to exit: ")
print(Back.GREEN + Fore.BLACK + "Game Ended!")