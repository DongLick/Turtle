
import random

player_score = 0
cpu_score = 0

number_of_games =  int(input('How many games do you want to play?\n'))

for i in range(number_of_games):
    computer_choice = random.choice(['scissors', 'rock', 'paper'])
    user_choice = input('do you want - rock, paper, or scissors?\n')
    print('computer has chosen:', computer_choice)
    if computer_choice == user_choice:
        print('TIE')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('WIN')
        player_score += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('WIN')
        player_score += 1
    elif user_choice == 'scissors'  and computer_choice == 'paper':
        print('win')
        player_score += 1
    else:
        print('You lose :( computeer wins :D')
        cpu_score += 1

print("player score", player_score)       
print("cpu score", cpu_score)       
        
    