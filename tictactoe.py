from tkinter import *
import random

window = Tk()
window.title("Tic-Ai")
#menu0 = Menu(window)


def game(row,col):
    if botons[row][col]["text"] == "" and check_win() == False :
        txt.config(text=( names[0] + " turn"))   
        botons[row][col]["text"] = players[0]
        if check_win() == True:
            txt.config(text=(names[0] + " wins!!"))
        elif check_win() == False:
             txt.config(text=(names[1] + " turn"))
             

        elif check_win() =='tie':
            txt.config(text="Nobody wins!!")

def check_empty_space():
    spaces = 9
    
    for row in range(3):
        for col in range(3):
            if botons[row][col]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else :
        return True

num = 0

def checkBotons():
    for row in range(3):
        for col in range(3):
            if botons[row][col] == 0:
                num += 1

def check_win():
    for row in range(3):
        if botons[row][0]["text"] == botons[row][1]["text"] == botons[row][2]["text"] != "":
            return True
        
    for col in range(3):
        if botons[0][col]["text"] == botons[1][col]["text"] == botons[2][col]["text"] != "":
            return True
        
    if botons[0][0]["text"] == botons[1][1]["text"] == botons[2][2]["text"] !="":
        return True
    
    if botons[2][0]["text"] == botons[1][1]["text"] == botons[0][2]["text"] !="":
        return True

    if check_empty_space() == False:
        for row in range(3):
            for col in range(3):
                botons[row][col].config(bg = 'red')
        return 'tie'
    else:
        return False

def isEmpy(row,col):
    if botons[row][col]["text"] == "" :
        return True
    else:
        return False

def start_new_game():
    txt.config(text=( names[0] + " turn"))

    for row in range(3):
        for col in range(3):
            botons[row][col].config(text="", bg = '#F0F0F0')

def isPlayer():
    if name == names[0]:
        return names[0]
    else:
        return names[1]

names = ["Player", "Ai"]
players = ["x", "o"]

botons = [[0, 0 ,0],
          [0, 0, 0],
          [0, 0, 0]
    ]

name = random.choice(names)
txt = Label(text=( name + " turn"), font=("arial", 40))
txt.pack(side="top")

restart= Button(text="Restart", font=("arial", 20), command=start_new_game, bg = 'grey')
restart.pack(side="top")

btn_frame = Frame(window)
btn_frame.pack()

for row in range(3):
    for col in range(3):
        botons[row][col] = Button(btn_frame, text="", font=("arial", 50), width=4, height=1 )
        botons[row][col].grid(row=row,column=col)
window.mainloop()