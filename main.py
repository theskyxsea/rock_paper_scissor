import random
import time
import winsound
print('WELCOME TO GAME')
print('ROCK PAPER SCISSOR')
choices=['rock','paper','scissor']
name = input('Your Name = ')
noofgames = int(input('How many matches you want to play = '))
score_comp = int(0)
score_user = int(0)
for i in range (noofgames):
    print('MATCH',end=' ')
    print(i+1)
    user_choice = str(input('Your Choice = '))
    comp_choice = str(random.choice(choices))
    if user_choice == choices[0] or user_choice == choices[1] or user_choice == choices[2]:
        print('and computer choose........')
        for i in range(3):
            time.sleep(1)
        print('Computer Choose = ' + comp_choice)
        print()
        if comp_choice == user_choice:
            print('Its a Tie..!')
        else:
            if user_choice == 'rock' :
                if comp_choice == choices[1]:
                    print('You Lose.!')
                    score_comp = score_comp+1
                else :
                    print('You Win..!')
                    score_user = score_user+1
            if user_choice == 'paper' :
                if comp_choice == choices[2]:
                    print('You Lose.!')
                    score_comp = score_comp + 1
                else :
                    print('You Win..!')
                    score_user = score_user + 1
            if user_choice == 'scissor' :
                if comp_choice == choices[0]:
                    print('You Lose.!')
                    score_comp = score_comp + 1
                else :
                    print('You Win..!')
                    score_user = score_user + 1
        print()
    else:
        print('Please restart and choice from rock, paper, scissor')
print('GAME OVER')
print('Final Scores ')
print('Computer Score = ', score_comp)
print(name + ' Score = ', score_user)
if score_user > score_comp:
    print()
    print(name + ' WIN..!')
    print('Congradulations...!')
    for i in range(3):
        if i != 2:
            for i in range(3):
                winsound.Beep(3800, 115)
                time.sleep(0.5)
            time.sleep(0.75)
        else:
            time.sleep(0.25)
            for i in range(3):
                winsound.Beep(3800, 150)
                time.sleep(0.70)
elif score_comp == score_user:
    winsound.Beep(2000, 300)
    time.sleep(1)
    print()
    print('Its a Tie..!')
else:
    print()
    print('Computer Win..!')