#    15-112: Principles of Programming and Computer Science
#    Project Programming: Connect - 4
#    Name      : Mohamed AL-Horr
#    AndrewID  : mahorr
#    File Created: Nov 9 2016
#    Modification History:
#    Start             End
#    Nov 9 9:00am      Nov 9 4:30pm
#    Nov 10 9:00am     Nov 10 3:00pm
#    Nov 11 11:00am     Nov 11 2:00pm
#    Nov 12 10:00am     Nov 12 1:00pm
#    Nov 13 4:00pm     Nov 13 6:00pm

import Tkinter as Tk
import tkMessageBox
import random
from PIL import Image, ImageTk



def Lmultiplayer():     # Function created to play local multiplayer
    global LMP
    wnd.destroy()
    LMP = 'yalla'
    return LMP

def printboard(b):                              #from TictacToe but greatly modifide
    global buttons
    global photoP1
    global photoP2
    for txt in range(len(b)):
        buttons[txt].configure(text=b[txt])
        if buttons[i] == 'P1':
            buttons[i].configure(image=photoP1)
        if buttons[i] == 'P2':
            buttons[i].configure(image=photoP2)           
        
def getElem(board,row,col):
    return board[row*3+col]

def getIndex(row,col):
    return row*3+col

def setElem(board,row,col,value):
    board[getIndex(row,col)]= value

def ButtonPressed(i):                       #from TictacToe but greatly modifide
    global gameboard
    global player
    global wnd
    global photoP1
    global photoP2
    global buttons
    imageP1 = Image.open("redplayer.png")
    photoP1 = ImageTk.PhotoImage(imageP1)
    imageP2 = Image.open("Yellowplayer.png")
    photoP2 = ImageTk.PhotoImage(imageP2)
    chars = ['P1','P2']
    result = 0
    if ifValid(gameboard,i+1):                  #inspierd from tictactoe but greatly modifide
        gameboard[i] = chars[player]
        if result == 1:
            msg =  "Player "+str(player)+" won"
        if result == 2:
            msg =  "Its a draw"
        player = (player+1)%2
        printboard(gameboard)
    if result != 0:
        msg = msg + "\n"+"Do you want to play again?"
        if tkMessageBox.askyesno(title ="Result",message=msg):
            resetGame()
        else:
            wnd.destroy()


def checkResult(board):                 #inspierd from Tictactoe but greatly modifide
    #Checking Rows
    if board[0] == board[1] and board[1] == board[2] and board[2] == board[3]:
        return 1
    if board[1] == board[2] and board[2] == board[3] and board[3] == board[4]:
        return 1
    if board[2] == board[3] and board[3] == board[4] and board[4] == board[5]:
        return 1
    if board[3] == board[4] and board[4] == board[5] and board[5] == board[6]:
        return 1
    if board[7] == board[8] and board[8] == board[9] and board[9] == board[10]:
        return 1
    if board[8] == board[9] and board[9] == board[10] and board[10] == board[11]:
        return 1
    if board[9] == board[10] and board[10] == board[11] and board[11] == board[12]:
        return 1
    if board[10] == board[11] and board[11] == board[12] and board[12] == board[13]:
        return 1
    if board[14] == board[15] and board[15] == board[16] and board[16] == board[17]:
        return 1
    if board[15] == board[16] and board[16] == board[17] and board[17] == board[18]:
        return 1
    if board[16] == board[17] and board[17] == board[18] and board[18] == board[19]:
        return 1
    if board[17] == board[18] and board[18] == board[19] and board[19] == board[20]:
        return 1
    if board[21] == board[22] and board[22] == board[23] and board[23] == board[24]:
        return 1
    if board[22] == board[23] and board[23] == board[24] and board[24] == board[25]:
        return 1
    if board[23] == board[24] and board[24] == board[25] and board[25] == board[26]:
        return 1
    if board[24] == board[25] and board[25] == board[26] and board[26] == board[27]:
        return 1
    if board[28] == board[29] and board[29] == board[30] and board[30] == board[31]:
        return 1
    if board[29] == board[30] and board[30] == board[31] and board[31] == board[32]:
        return 1
    if board[30] == board[31] and board[31] == board[32] and board[32] == board[33]:
        return 1
    if board[31] == board[32] and board[32] == board[33] and board[33] == board[34]:
        return 1
    if board[35] == board[36] and board[36] == board[37] and board[37] == board[38]:
        return 1
    if board[36] == board[37] and board[37] == board[38] and board[38] == board[39]:
        return 1
    if board[37] == board[38] and board[38] == board[39] and board[39] == board[40]:
        return 1
    if board[38] == board[39] and board[39] == board[40] and board[40] == board[41]:
        return 1
    #checking for draw
    if board.count('X') + board.count('O') == 9:
        return 2
    return 0

def ifValid(board,m):               #from TicTacToe but greatly modifide
    if m<1 or m > 42:
        return False
    if board[m-1] == 'P1' or board[m-1] == 'P2':
        return False
    return True

def processInput(board,m,p):                    #from tictactoe but greatly modifide
    chars = ['P1','P2']
    if board[m+7] != 'P1' and board[m+14] != 'P1' and board[m+21] != 'P1' and board[m+28] != 'P1' and board[m+35]!= 'P1' or (board[m+7] != 'P2' and board[m+14] != 'P2' and board[m+21] != 'P2' and board[m+28] != 'P2' and board[m+35]!= 'P2'):
        board[m+35] = chars[p]
    if board[m+7] != 'P1' and board[m+14] != 'P1' and board[m+21] != 'P1' and board[m+28] != 'P1' or (board[m+7] != 'P2' and board[m+14] != 'P2' and board[m+21] != 'P2' and board[m+28] != 'P2'):
        board[m+28] = chars[p]
    if board[m+7] != 'P1' and board[m+14] != 'P1' and board[m+21] != 'P1' or (board[m+7] != 'P2' and board[m+14] != 'P2' and board[m+21] != 'P2'):
       board[m+21] = chars[p]
    if board[m+7] != 'P1' and board[m+14] != 'P2' or (board[m+7] != 'P2' and board[m+14] != 'P2'):
        board[m+14] = chars[p]
    if board[m+7] != 'P1' or board[m+7] != 'P1':
        board[m+7] = chars[p]
    else:
        board[m-1] = chars[p]



gameboard = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42".split()
result = 0
player = 0
LMP = ''
buttons = []
photoP1 = None
photoP2 = None


wnd = Tk.Tk()                           #main menu for game
wnd.title("Connect 4")
wnd.geometry("600x400")
wnd.configure(bg='Blue')
Menulable = Tk.Label(wnd,text = "Connect 4",fg = 'yellow',bg= 'blue',height = 6,font=("Helvetica", 40))
Menulable.pack()
splay = Tk.Button(wnd, text='Single Player',bg= 'blue',font=("Helvetica", 18),)
splay.pack()
lplay = Tk.Button(wnd, text='Local Multiplayer',bg= 'blue',font=("Helvetica", 18), command = Lmultiplayer)
lplay.pack()
mplay = Tk.Button(wnd, text='Multiplayer',font=("Helvetica", 18), background= 'light blue')
mplay.pack()
wnd.mainloop()


if LMP == 'yalla':                      #main code of local multiplayer
    Lp = Tk.Tk()
    Lp.title("Connect 4")
    Lp.geometry("640x490")
    Lp.configure(bg = 'blue')
    image = Image.open("TranspBg.png")
    photo = ImageTk.PhotoImage(image)

    for i in range(42):
        b = Tk.Button(Lp,image=photo,text=str(i+1),height=55,width = 65,fg ='blue', command = lambda x=i:ButtonPressed(x))
        b.grid(row=i/7, column=i%7,padx = 9.35,pady = 7.75)
        buttons.append(b.cget("text"))
    Lp.mainloop()

