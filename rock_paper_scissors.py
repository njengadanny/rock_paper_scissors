import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox

win = 0
tie = 0
lose = 0

def game(user):
    global win
    global tie
    global lose
    
    #computer choice
    comp_choice = ['Rock', 'Paper', 'Scissors']
    comp_choice = random.choice(comp_choice)
    
    if user == comp_choice:
        result = 'tied'
    elif (user == 'Rock' and comp_choice == 'Paper') or (user == 'Paper' and comp_choice == 'Scissors') or (user == 'Scissors' and comp_choice == 'Rock'):
        result = 'lose'
    else:
        result = 'win'
                
    if result == 'tied':
        tie += 1
    elif result == 'lose':
        lose += 1
    else:
        win += 1
    times_played = win + lose + tie

    lbl_result['text'] = "You played %s, Therefore you %s!" %(user, result)
    lbl_score['text'] = 'Score:\nYou: %s\nComputer: %s\nTies: %s\n Games played: %s' %(win, lose, tie, times_played)
    lbl_comp_choice['text'] = 'Computer choice: \n%s' %(comp_choice)

m = tk.Tk()
m.title('Rock Paper Scissors Game')
m.geometry('500x300')
m['bg'] = '#999966'

label_1 = tk.Label(m, text = 'Make your selection:', font = ("Comic Sans MS", 15))
label_1.pack(side=TOP)
label_1['bg'] = "#999966"

rockbutton = tk.Button(m, text='Rock', width=20, bg="#339966", fg="black", font = ('bold'),command = lambda: game('Rock'))
paperbutton = tk.Button(m, text='Paper', width=20, bg="white", font = ('bold'),command = lambda: game('Paper'))
scissorsbutton = tk.Button(m, text='Scissors', width=20, bg="#336699", font = ('bold'),command = lambda: game('Scissors'))
rockbutton.pack()
paperbutton.pack()
scissorsbutton.pack()

label_2 = tk.Label(m, text = 'Result:', font = ("Comic Sans MS", 15))                     
label_2.pack()
label_2['bg'] = "#999966"

lbl_result = Label(m, font = ("Comic Sans MS", 10, 'bold'))
lbl_result.pack()
lbl_result['bg'] = "#999966"

lbl_score = Label(m, text = 'Score:\nYou: 0\nComputer: 0\nTies: 0\n Games played: 0', font = ("Comic Sans MS", 10, 'bold'))
lbl_score.pack()
lbl_score['bg'] = "#999966"

lbl_comp_choice = Label(m, font = ("Comic Sans MS", 10, 'bold'))
lbl_comp_choice.pack()
lbl_comp_choice.place(x=350, y=70)
lbl_comp_choice['bg'] = "#999966"

def instruct():
    messagebox.showinfo("Instructions", "Rock beats Scissors\nPaper beats Rock\nScissors beats Paper\nAnd it's obvious what happens when the same elemnts are selected")
        
def about():
    messagebox.showinfo("About", "This game is developed by Danny Njenga.")

menu = Menu(m)
m.config(menu=menu)
filemenu = Menu(menu)
filebutton = menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Instructions', command=instruct)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=m.destroy)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=about)



m.mainloop()