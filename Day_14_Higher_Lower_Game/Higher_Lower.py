from logo import logo
from logo import vs
from data import data
import random
from replit import clear


def pick_random_account(data):
    person = data[random.randint(0,len(data)-1)]
    return person

def print_description(person, a):
    if a == 'A':
        print(f"Compare {a}: {person['name']}, a {person['description']}, from {person['country']}.")
    else:
        print(f"Against {a}: {person['name']}, a {person['description']}, from {person['country']}.")

def play_a_game(data):

    person_one = pick_random_account(data)
    print_description(person_one, 'A')
    follower_p_one = person_one['follower_count']
    print(vs)
    person_two = pick_random_account(data)

    while (person_one == person_two):
        person_two = pick_random_account(data)
    print_description(person_two, 'B')
    follower_p_two = person_two['follower_count']
    if compare(person_one, person_two, follower_p_one, follower_p_two) == 0:
        return 0
    return 1


def compare(person_one, person_two, follower_p_one, follower_p_two):
    while True:
        answer = input("\nWho has more followers? Type 'A' or 'B': ")
    
        if answer == 'A' and follower_p_one > follower_p_two:
            print(f"NICE, {person_one['name']} has {follower_p_one} while {person_two['name']} has {follower_p_two} ")
            return 0
        elif answer == 'A' and follower_p_one < follower_p_two:
            print(f"Sorry... {person_one['name']} has {follower_p_one} while {person_two['name']} has {follower_p_two} ")
            return 1
        elif answer == 'B' and follower_p_one > follower_p_two:
            print(f"Sorry... {person_one['name']} has {follower_p_one} while {person_two['name']} has {follower_p_two} ")
            return 1
        elif answer == 'B' and follower_p_one < follower_p_two:
            print(f"NICE, {person_two['name']} has {follower_p_two} while {person_one['name']} has {follower_p_one} ")
            return 0
        else:
            print("Invalid input. Please type 'A' or 'B'.")


game = True
score = 0
while game:
    #print(logo)
    print(f"\nYour current score is: {score}")
    retry = 'Y'
    if play_a_game(data) == 1:
        print(f"You finish with a score of {score}")
        retry = input("Rematch? Type 'Y' or 'N': ")
        score = 0
    else:
        score  += 1
    if retry == 'N':
        print("Thanks For playing with us!")
        game = False
    clear()
    