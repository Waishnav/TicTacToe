from time import sleep
import random

print('''
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█                           X ║ O ║
█░ ╦ ╦╔╗╦ ╔╗╔╗╔╦╗╔╗ ░█                          ═══║═══║═══
█░ ║║║╠ ║ ║ ║║║║║╠  ░█   to play Tick-Tack-Toe     ║ X ║ O
█░ ╚╩╝╚╝╚╝╚╝╚╝╩ ╩╚╝ ░█                          ═══║═══║═══
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█                           O ║   ║ X
''')

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

'''
   ║   ║
═══║═══║═══
   ║   ║
═══║═══║═══
   ║   ║
'''

Board = {'7': ' ', '8': ' ', '9': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '1': ' ', '2': ' ', '3': ' '}
unfilled_list = ['1','2','3','4','5','6','7','8','9']
# printing board function with Num-pad gui visualization
def printBoard(board):
    print(" "+ board['7'] , '║' , board['8'] , '║' + board['9'],"       7 | 8 | 9 ")
    print('═══║═══║═══     ---|---|---')
    print(" "+ board['4'] , '║' , board['5'] , '║' + board['6'],"       4 | 5 | 6 ")
    print('═══║═══║═══     ---|---|---')
    print(" "+ board['1'] , '║' , board['2'] , '║' + board['3'],"       1 | 2 | 3 ")

won = False

def print_thinking():
    list = ["⚪ ◉ ◉ ", "◉ ⚪ ◉ ", "◉ ◉ ⚪ ","⚪ ◉ ◉ ", "◉ ⚪ ◉ ", "◉ ◉ ⚪ ","⚪ ◉ ◉ ", "◉ ⚪ ◉ ", "◉ ◉ ⚪ "]
    for i in range(len(list)):
        print(list[i], sep='', end='\r', flush=True)
        sleep(0.2)

# win_conditions = checkpost at every moves from both user which checks vertical horrizontal and diagonal symmetry
def win_conditions(y):
    global won
    if Board['7']==Board['8']==Board['9']== y or Board['4']==Board['5']==Board['6']== y or Board['1']==Board['2']==Board['3']== y:
        won = True
        print(color.BOLD + color.BLUE + y,"won the game" + color.END)
    elif Board['7']==Board['4']==Board['1']== y or Board['8']==Board['5']==Board['2']== y or Board['9']==Board['6']==Board['3']== y:
        won = True
        print(color.BOLD + color.BLUE + y,"won the game" + color.END)
    elif Board['7']==Board['5']==Board['3']== y or Board['1']==Board['5']==Board['9']== y:
        won = True
        print(color.BOLD + color.BLUE + y,"won the game" + color.END)

#  game (playing with another friend)
def game1():
    moves_count = 0
    X_turn = True
    # win_conditions = checkpost at every moves from both user vertical horrizontal and diagonal symmetry
    global won
    while moves_count != 9 and not won:
        if X_turn:
            printBoard(Board)
            print("Its X's turn,")
            move = input()
            if int(move) > 9:
                print("you have mistakenly given wrong input...")
            elif Board[move] == ' ':
                Board[move] = "X"
                moves_count += 1
                a = "X"
                win_conditions(a)
                X_turn = False
            else:
                print("\nOops its already filled. \nMove to which place?")
        else:
            printBoard(Board)
            print("Its O's turn.")
            move = input()
            if int(move) > 9:
                print("you have mistakenly given wrong input...")
            elif Board[move] == ' ':
                Board[move] = "O"
                moves_count += 1
                a = "O"
                win_conditions(a)
                X_turn = True
            else:
                print("\nOops its already filled. \nMove to which place?")

# palying with computer
def game2():
    moves_count = 0
    X_turn = True
    # win_conditions = checkpost at every moves from both user vertical horrizontal and diagonal symmetry
    global won
    while moves_count != 9 and not won:
        if X_turn:
            printBoard(Board)
            print("Its X's (your) turn,")
            move = input()
            if int(move) > 9:
                print("you have mistakenly given wrong input...")
            elif Board[move] == ' ':
                Board[move] = "X"
                moves_count += 1
                a = "X"
                win_conditions(a)
                unfilled_list.remove(move)
                X_turn = False
            else:
                print("\nOops its already filled. \nMove to which place?")
        else:
            printBoard(Board)
            print("Its COMPUTER's turn.")
            #statement = "Computer is thinking..."
            #for t in statement:
            #    print(statement[t], sep='', flush=True); sleep(0.2)
            print_thinking()
            move = random.choice(unfilled_list)
            if Board[move] == ' ':
                Board[move] = "O"
                moves_count += 1
                a = "O"
                win_conditions(a)
                unfilled_list.remove(move)
                X_turn = True


print('1. Play with your friend')
print('2. Play with computer')
choice = input("Which mode do u want to select 1 or 2??\n")
print("First of all you need to understand how you are gonna play this game")
print("Keyboard Numpad is used as input device corresponding to each position")

if choice == '1':
    game1()
    printBoard(Board)
elif choice == '2':
    game2()
    printBoard(Board)
else:
    print('Wrong Choice')
