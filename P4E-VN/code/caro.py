#!/usr/bin/python
# -*- coding: utf8 -*-
#Chương trình caro dành cho 2 người chơi.
board = [0,1,2,3,4,5,6,7,8,]

def o_con_trong():
    for x in range(0,9):
        if board[x] != 'x' and board[x] != 'o':
            return True
def check_line(ch,x1,x2,x3):
    if board[x1] == ch and board[x2] == ch and board[x3] == ch:
        return True
    return False
def check_all(ch):
    if check_line(ch, 0, 1, 2):
        return True
    if check_line(ch, 3, 4, 5):
        return True
    if check_line(ch, 6, 7, 8):
        return True
    if check_line(ch, 0, 4, 8):
        return True
    if check_line(ch, 6, 4, 2):
        return True
    if check_line(ch, 0, 3, 6):
        return True
    if check_line(ch, 1, 4, 7):
        return True
    if check_line(ch, 2, 5, 8):
        return True

    return False

def print_board(x1,x2,x3):
    print board[x1], '|' , board[x2], '|' , board[x3]
    print '---------'
def show_board():
    print_board(0,1,2)
    print_board(3,4,5)
    print_board(6,7,8)
show_board()

win = 0

while o_con_trong():
    player1 = raw_input("Nhập vào một số tương ứng với nước đi (Player1) : ")
    player1 = int(player1)

    if board[player1] == 'o' or board[player1] == 'x':
        print "Ô này đã được chọn, hãy chọn lại ô khác !!!"
    else:
        board[player1] = 'x'
        while o_con_trong():
            player2 = raw_input("Nhập vào một số tương ứng với nước đi (Player2) : ")
            player2 = int(player2)
            if board[player2] == 'x' or board[player2] == 'o':
                pass
            else:
                board[player2] = 'o'
                break
    show_board()

    if check_all('x'):
        print "Bạn đã chiến thắng !!!"
    if check_all('o'):
        print "Máy thắng !!!"
        break
if win == 0:
    print "Hòa !!!"
else:
    print win, 'CHiến thắng !!!'



