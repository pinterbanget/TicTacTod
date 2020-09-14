#! python3

import random
import sys
import time

def printboard(B):
    #untuk menampilkan board dalam layar.
    print('')
    print(B[7] + '│' + B[8] + '│' + B[9])
    print('‒‒‒‒‒')
    print(B[4] + '│' + B[5] + '│' + B[6])
    print('‒‒‒‒‒')
    print(B[1] + '│' + B[2] + '│' + B[3])
    print('')
   
def choose():
    #untuk memberikan pilihan kepada user, mau X atau O.
    while True:
        char = str.upper(input('Mau jadi X atau O? : '))
        if char == 'X' or char == 'O' or char == '1' or char == '2':
            break
        print('Mohon masukkan X atau O.')
        
    if char == 'X' or char == '1':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
def firstmove():
    #untuk menentukan siapa yang jalan duluan, diacak menggunakan random.randint.
    if random.randint(1, 2) == 1:
        return 'tAI'
    else:
        return name

def wincond(b, c):
    #memberikan winning condition
    return ( \
    (b[7] == c and b[8] == c and b[9] == c) or #top x-axis
    (b[4] == c and b[5] == c and b[6] == c) or #mid x-axis
    (b[1] == c and b[2] == c and b[3] == c) or #bot x-axis
    (b[7] == c and b[5] == c and b[3] == c) or #diagonal 1
    (b[9] == c and b[5] == c and b[1] == c) or #diagonal 2
    (b[7] == c and b[4] == c and b[1] == c) or #left y-axis
    (b[8] == c and b[5] == c and b[2] == c) or #mid y-axis
    (b[9] == c and b[6] == c and b[3] == c))   #right y-axis
        
def turnmove(boardd, char, move):
    #untuk mengisi list [board] dengan character (X atau O)
    boardd[move] = char

def freespace(boardd, move):
    #untuk mengecek list [board] udah keisi atau blom
    return boardd[move] == ' '

def copyboardforcom(boardd):
    #bikin board duplicate for AI calculations
    copyboard = []
    for i in boardd:
        copyboard.append(i)
        
    return copyboard

def playermove(boardd):
    #buat jalan player
    move = ' '   
    while True:
        try:
            move = int(input('Pilih mau jalan ke kotak mana (1-9): '))
            if move < 1 or move > 9:
              print('Mohon masukkan angka 1-9.')
            #'1-9'.split() = bikin list isinya 1 sampe 9
            elif move in '1 2 3 4 5 6 7 8 9'.split() or freespace(boardd, move):
                break
            else:
                print('Kotak sudah diisi. Mohon masukkan angka lain.')
        except ValueError:
            print('Mohon masukkan angka 1-9.')

    return move

def randommove(boardd, movelist):
    #buat AI, klu ga butuh set moves, biar ambil kotak random yang masi kosong
    possiblemoves = []
    for i in movelist:
        if freespace(boardd, i):
            possiblemoves.append(i)
            
    if len(possiblemoves) != 0:
        return random.choice(possiblemoves)
    else:
        return None

def commove(boardd, comchar):
    #AI. refer to set conditions
    if comchar == 'X':
        playerchar = 'O'
    else:
        playerchar = 'X'
    
    moveEdge = randommove(boardd, [2, 4, 6, 8])
    moveCorner = randommove(boardd, [1, 3, 7, 9])
    moveAll = randommove(boardd, [1, 2, 3, 4, 6, 7, 8, 9])
    
    #cond 1: bisa menang
    for i in range (1, 10):
        copy = copyboardforcom(boardd)
        if freespace(copy, i):
            turnmove(copy, comchar, i)
            if wincond(copy, comchar):
                return i
            
    #cond 2: bisa ngalangin
    for i in range (1,10):
        copy = copyboardforcom(boardd)
        if freespace(copy, i):
            turnmove(copy, playerchar, i)
            if wincond(copy, playerchar):
                return i
            
    #cond 3: ambil tengah
    copy = copyboardforcom(boardd)
    if freespace(boardd, 5):
        return 5
    
    if board[5] == comchar:
        #cond 4: setcond 1a, CC jauh.
        if setcond1a(copy, playerchar):
            return moveEdge
            
        #cond 5: setcond 2, EE deket.
        elif freespace(boardd, 1) and freespace(boardd, 3)\
        and freespace(boardd, 7) and freespace(boardd, 9):
            return setcond2()
          
        #cond 6: setcond 3, CE jauh.
        elif 1 not in SC3:
            SC3.append(1)
            return setcond3()
        
        else: #just in case.
            return moveAll
          
    elif board[5] == playerchar:
        #cond 7: setcond 1b, NC jauh dengan corner kita.
        if setcond1b(copy, playerchar):
            if freespace(boardd, 1) or freespace(boardd, 3)\
            or freespace(boardd, 7) or freespace(boardd, 9):
                return moveCorner
            else:
                return moveEdge
        
        #cond 2ndtoLAST: ambil corner acak
        elif freespace(boardd, 1) or freespace(boardd, 3)\
        or freespace(boardd, 7) or freespace(boardd, 9):
            return moveCorner
    
        #cond LAST: ambil samping acak
        else:
            return moveEdge
    
    else:
        return moveAll

def fullboard(boardd):
    #buat cek boardnya uda penuh atau blom.
    for i in range (1, 10):
        if freespace(boardd, i):
            return False
    return True

#AI set conditions
def setcondfree(boardd, move):
    if freespace(boardd, move):
        return move
    else:
        return randommove(board, [1, 3, 7, 9])
    
def setcond1a(b, c): #CC jauh. set condition = diagonal
    return ( \
    (b[1] == c and b[9] == c) or \
    (b[7] == c and b[3] == c))

def setcond1b(b,c): #NC jauh ke corner kita. set condition = diagonal
    return ( \
    (b[1] == c and b[5] == c) or \
    (b[7] == c and b[5] == c) or \
    (b[5] == c and b[9] == c) or \
    (b[5] == c and b[3] == c))

def setcond2(): #EE deket, go to corner yang diapit. set condition: 4 cond.
    if board[4] == playerchar and board[2] == playerchar:
        return setcondfree(board, 1)
    elif board[6] == playerchar and board[2] == playerchar:
        return setcondfree(board, 3)
    elif board[4] == playerchar and board[8] == playerchar:
        return setcondfree(board, 7)
    elif board[6] == playerchar and board[8] == playerchar:
        return setcondfree(board, 9)
    else:
        return randommove(board, [1, 3, 7, 9])

def setcond3(): #CE jauh, go to C lowest distance dari C ke E nya dia. set condition: 8 cond.
    if board[3] == playerchar and board[4] == playerchar\
    or board[7] == playerchar and board[2] == playerchar:
        return setcondfree(board, 1)
    elif board[1] == playerchar and board[6] == playerchar\
    or board[9] == playerchar and board[2] == playerchar:
        return setcondfree(board, 3)
    elif board[9] == playerchar and board[4] == playerchar\
    or board[1] == playerchar and board[8] == playerchar:
        return setcondfree(board, 7)
    elif board[3] == playerchar and board[8] == playerchar\
    or board[7] == playerchar and board[6] == playerchar:
        return setcondfree(board, 9)
    else:
        return randommove(board, [1, 3, 7, 9])
    
print('Selamat datang dalam permainan Tic-Tac-Toe.')
print('Aku tAI, AI Tic-Tac-Toe yang tidak pernah akan kalah.')
name = str(input('Siapa namamu?: '))
print('Halo, %s. Senang bertemu denganmu.' % (name))
print('Untuk tutorial bermain, ketik "T".')
comScore = 0
playerScore = 0
tieScore = 0
           
while True:
    SC3 = [] #special trigger for setcond3 supaya keexecute cuman sekali
    board = [' '] * 10
    maingak = str.lower(input('Untuk memulai permainan, ketik "M". Untuk keluar permainan, ketik "K": '))
    
    if maingak == 'm' or maingak == '1':
        playerchar, comchar = choose()
        turn = firstmove()
        print(turn + ' jalan duluan, ya.')
        
        while True:
            if turn == name:
                printboard(board)
                move = playermove(board)
                turnmove(board, playerchar, move)
                
                if wincond(board, playerchar):
                    printboard(board)
                    playerScore += 1
                    print('Selamat, %s! Kamu menang. Curang ya?' % (name))
                    print('Skor: tAI %s - %s %s (%s seri)' % (comScore, playerScore, name, tieScore))
                    break
                
                else:
                    if fullboard(board):
                        printboard(board)
                        tieScore += 1
                        print('Wah, seri nih kita!')
                        print('Skor: tAI %s - %s %s (%s seri)' % (comScore, playerScore, name, tieScore))
                        break
                        
                    else:
                        turn = 'tAI'
            
            else:
                time.sleep(0.1)
                move = commove(board, comchar)
                turnmove(board, comchar, move)
                
                if wincond(board, comchar):
                    printboard(board)
                    comScore += 1
                    print('Haha! Kamu belum bisa mengalahkanku.')
                    print('Skor: tAI %s - %s %s (%s seri)' % (comScore, playerScore, name, tieScore))
                    break
                
                else:
                    if fullboard(board):
                        printboard(board)
                        tieScore +=1
                        print('Wah, seri nih kita!')
                        print('Skor: tAI %s - %s %s (%s seri)' % (comScore, playerScore, name, tieScore))
                        break
                        
                    else:
                        turn = name
                    
    elif maingak == 'k' or maingak == '2':
        break
    
    elif maingak == 't':
        print('Cara bermain Tic-Tac-Toe:')
        print('')
        print('7' + '│' + '8' + '│' + '9')
        print('‒‒‒‒‒')
        print('4' + '│' + '5' + '│' + '6')
        print('‒‒‒‒‒')
        print('1' + '│' + '2' + '│' + '3')
        print('')
        print('Layout yang keluar berbentuk seperti itu, mengikuti bentuk numpad.')
        print('Untuk menaruh piece, ketik angka yang sesuai dengan nomor kotak.')
        print('Contoh: jika ingin menaruh piece di kotak tengah, ketik "5".')
        print('')
        print('Tips: selain mengetik M atau K, kalian juga bisa mengetik 1 untuk mulai dan 2 untuk keluar.')
        print('Kalian juga bisa mengetik 1 untuk X dan 2 untuk O.')
    
    else:
        print('Mohon masukkan kode yang benar.')
        
print('Terima kasih telah bermain Tic-Tac-Toe, %s. Semoga harimu menyenangkan.' % (name))
sys.exit()
