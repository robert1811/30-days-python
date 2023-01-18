your_score = 0
cpu_score = 0

import random

choices = ['rock', 'paper', 'scissors']


def play():
    def print_score():
        global your_score
        global cpu_score
        print('Your score: ' + str(your_score))
        print('CPU score: ' + str(cpu_score))

    def win():
        print('You won')
        global your_score
        your_score += 1
        print_score()
        play()

    def lose():
        print('You lose')
        global cpu_score
        cpu_score += 1
        print_score()
        play()

    def draw():
        print('Its a draw')
        print_score()
        play()
        
        
    player_choice = input('Rock, paper or scissors? ')
    cpu_choice = random.choice(choices)
    print('You selected {}'.format(player_choice))
    print('He selected {}'.format(cpu_choice))

    if player_choice.lower() == 'rock':
        if cpu_choice == 'scissors':
            win()
        elif cpu_choice == 'paper': 
            lose()
        else:
            draw()
    elif player_choice.lower() == 'paper':
        if cpu_choice == 'scissors':
            lose()
        elif cpu_choice == 'paper':
            draw()
        else:
            win()
    elif player_choice.lower() == 'scissors':
        if cpu_choice == 'scissors':
            draw()
        elif cpu_choice == 'paper':
            win()
        else:
            lose()
    else:
        play()
            
play()