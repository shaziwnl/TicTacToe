import tkinter as Tk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe Game")

# By default no button is clicked so false
clicked = False

# Count keeps track of the number of moves
count = 0

# Button Click Function
def b_click(b):
    global clicked,count
    if b["text"] == " " and clicked == False:
        b["text"] = "X"
        clicked = True
        count += 1
        wincheck()
        if count==9:
            messagebox.showinfo("Tic-Tac-Toe","Draw!")
    elif b["text"] == " " and clicked == True:
        b["text"] = "O"
        clicked = False
        count += 1
        wincheck()
    else:
        messagebox.showerror("Tic-Tac-Toe","Button has already been clicked!")

# Win checker
def wincheck():
    global winner
    winner = False

    if ((b1["text"] == "X" and b3["text"] == "X" and b2["text"] == "X") or
        (b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X") or
        (b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X") or
        (b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X") or
        (b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X") or
        (b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X") or
        (b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X") or
        (b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X")):
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X WINS!")
        disable_buttons()
    elif ((b1["text"] == "O" and b3["text"] == "O" and b2["text"] == "O") or
        (b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O") or
        (b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O") or
        (b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O") or
        (b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O") or
        (b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O") or
        (b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O") or
        (b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O")):
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O WINS!")
        disable_buttons()

# Disabling buttons after game is over
def disable_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# Restart
def restart():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked,count
    clicked = False
    count = 0
    # Making the buttons
    b1 = Button(root, text=" ", font=("MS Serif", 25), height=2,width=6, bg="white", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("MS Serif", 25), height=2,width=6, bg="white", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("MS Serif", 25), height=2,width=6, bg="white", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("MS Serif", 25), height=2,width=6, bg="white", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("MS Serif", 25), height=2,width=6, bg="white", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("MS Serif", 25), height=2,width=6, bg="white", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("MS Serif", 25), height=2,width=6, bg="white", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("MS Serif", 25), height=2,width=6, bg="white", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("MS Serif", 25), height=2,width=6, bg="white", command=lambda: b_click(b9))

    # Making the grid
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)



# Menu
tictac_menu= Menu(root)
root.config(menu=tictac_menu)

# Options Menu
options_menu = Menu(tictac_menu, tearoff= False)
tictac_menu.add_command(label="Restart", command=restart)

restart()
root.mainloop()
