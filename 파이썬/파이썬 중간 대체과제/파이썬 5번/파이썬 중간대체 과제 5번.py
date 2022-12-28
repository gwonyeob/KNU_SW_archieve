import sys
global position
def printBoard(board):
    print("  -----------")
    print(" | " + board[1] + " | " + board[2] + " | " + board[3] + " |")
    print("  -----------")
    print(" | " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("  -----------")
    print(" | " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("  -----------")



def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (check_draw()):
            print("아쉽지만 무승부입니다!")
            sys.exit()
        if check_win():
            if letter == 'X':
                print("컴퓨터의 승리입니다 분발하세요!")
                sys.exit()
            else:
                print("축하합니다 당신의 승리입니다!")
                sys.exit()
        return
    else:
        print("이곳은 놓을 수 없는 자리입니다")
        position = int(input("놓을 곳을 입력하세요:  "))
        insertLetter(letter, position)
        return


def check_win():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkwhichplayerwin(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def check_draw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def player_move():
    print("당신의 차례입니다!")
    x=int(input("X좌표를 입력하세요 >> "))
    y=int(input("Y좌표를 입력하세요 >> "))
    if x==1:
        if y==1:
            position=1
        elif y==2:
            position=2
        elif y==3:
            position=3
    if x==2:
        if y==1:
            position=4
        elif y==2:
            position=5
        elif y==3:
            position=6
    if x==3:
        if y==1:
            position=7
        elif y==2:
            position=8
        elif y==3:
            position=9
    insertLetter(player, position)
    return


def com_move():
    print("컴퓨터의 차례입니다!")
    bestscore = -2022
    bestmove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestscore):
                bestscore = score
                bestmove = key

    insertLetter(bot, bestmove)
    return


def minimax(board, depth, isMaximizing):
    if (checkwhichplayerwin(bot)):
        return 1
    elif (checkwhichplayerwin(player)):
        return -1
    elif (check_draw()):
        return 0

    if (isMaximizing):
        bestscore = -2022
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestscore):
                    bestscore = score
        return bestscore

    else:
        bestscore = 2022
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestscore):
                    bestscore = score
        return bestscore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printBoard(board)
player = 'O'
bot = 'X'

while not check_win():
    player_move()
    com_move()