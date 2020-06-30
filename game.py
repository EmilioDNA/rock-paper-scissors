# Write your code here
import random
import math 


def get_score(file, name):
    file_opened = open(file, 'r', encoding='utf-8')
    players = file_opened.readlines()
    players_dict = {player.split(' ')[0]: player.split(' ')[1].strip('\n') for player in players}
    if name in players_dict:
        return int(players_dict[name])
    else:
        return 0


def slice_options(game_options, selected_option):
    index = game_options.index(selected_option)
    new_list = game_options[index + 1:] + game_options[:index]
    return new_list


# The main program starts
player_name = input("Enter your name ")
print(f"Hello, {player_name}")

choices = input().split(',')
if len(choices) == 1:
    choices = ['rock', 'paper', 'scissors']

print(choices)
print()
print("Okay, let's start")

score = get_score('rating.txt', player_name)

choice = ""
while choice != "!exit":
    choice = input()
    if choice == '!rating':
        print(f'Your rating: {score}')
    elif choice == '!exit':
        print('Bye!')
        break
    elif choice not in choices:
        print('Invalid input')
        continue
    else:
        computer_option = math.floor(random.random() * len(choices))
        decision = ''
        computer_move = choices[computer_option]
        if choice == computer_move:
            decision = f'There is a draw ({choice})'
            score += 50
        else:
            clean_choices = slice_options(choices, choice)
            middle = int(len(clean_choices) / 2)
            if computer_move in clean_choices[middle:]:
                decision = f'Well done. Computer chose {computer_move} and failed'
                score += 100
            else:
                decision = f'Sorry, but computer chose {computer_move}'
        print(decision)