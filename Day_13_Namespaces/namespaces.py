
from logo import logo
import random
from replit import clear



def time_to_play(remaining_mooves, number_guess):
    player_number = 0
    while remaining_mooves > 0 and number_guess != player_number:
        player_number = int(input("Pick a number between 1 and 100: "))
        if player_number > number_guess:
            print("To high !")
            remaining_mooves -= 1
            print(f"remaining_mooves: {remaining_mooves}")
        elif player_number < number_guess:
            print("To low !")
            remaining_mooves -= 1
            print(f"remaining_mooves: {remaining_mooves}")
    if remaining_mooves == 0:
        return 1
    else:
        return 0

def game():
    number_guess = random.randint(1, 100)
    remaining_mooves = 10
    if input("Choose a difficulty: 'hard' or 'easy': ") == 'hard':
        remaining_mooves = 5
    if time_to_play(remaining_mooves, number_guess) == 0:
        print("\n!!!!! GG !!!!!")
        print("Congratulation you WIN !!!\n")
    else:
        print("Sorry, You Loose ...")

play = True

while play:
    print(logo)
    game()
    if input("Do you want to play another game ? 'y' or 'n': ") == 'n':
        play = False
        print("Thanks for playing with us!!")
    clear()
    
    