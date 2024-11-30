import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for comb in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[comb[0]]["text"] == buttons[comb[1]]["text"] == buttons[comb[2]]["text"] != "":
            buttons[comb[0]].config(bg="green")
            buttons[comb[1]].config(bg="green")
            buttons[comb[2]].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[comb[0]]['text']} wins!")
            root.quit()
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        root.quit()

def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:  
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
winner = False

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, 
            command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
