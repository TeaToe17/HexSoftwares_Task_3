import tkinter as tk
from tkinter import messagebox
import random
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Puzzle Game")
        self.root.geometry("400x450")
        self.buttons = {}
        self.cards = list("AABBCCDDEEFF")
        random.shuffle(self.cards)
        self.flipped = []
        self.matched = []
        self.time_limit = 60
        self.start_time = time.time()
        
        self.create_widgets()
        self.update_timer()

    def create_widgets(self):
        self.timer_label = tk.Label(self.root, text=f"Time left: {self.time_limit} seconds", font=("Arial", 14))
        self.timer_label.pack(pady=10)
        
        grid_frame = tk.Frame(self.root)
        grid_frame.pack()

        for i in range(4):
            for j in range(3):
                btn = tk.Button(grid_frame, text="?", width=6, height=3,
                                command=lambda i=i, j=j: self.flip_card(i, j))
                btn.grid(row=i, column=j)
                self.buttons[(i, j)] = btn

    def flip_card(self, row, col):
        if (row, col) in self.matched or len(self.flipped) == 2:
            return

        card_index = row * 3 + col
        card_value = self.cards[card_index]
        self.buttons[(row, col)].config(text=card_value, state="disabled")
        self.flipped.append((row, col))

        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        (row1, col1), (row2, col2) = self.flipped
        card1 = self.cards[row1 * 3 + col1]
        card2 = self.cards[row2 * 3 + col2]

        if card1 == card2:
            self.matched.append((row1, col1))
            self.matched.append((row2, col2))
        else:
            self.buttons[(row1, col1)].config(text="?", state="normal")
            self.buttons[(row2, col2)].config(text="?", state="normal")
        
        self.flipped = []

        if len(self.matched) == len(self.cards):
            self.end_game(win=True)

    def update_timer(self):
        time_left = self.time_limit - int(time.time() - self.start_time)
        self.timer_label.config(text=f"Time left: {time_left} seconds")

        if time_left <= 0:
            self.end_game(win=False)
        else:
            self.root.after(1000, self.update_timer)

    def end_game(self, win):
        if win:
            messagebox.showinfo("Memory Puzzle", "Congratulations! You won!")
        else:
            messagebox.showinfo("Memory Puzzle", "Time's up! You lost!")

        for btn in self.buttons.values():
            btn.config(state="disabled")

root = tk.Tk()
game = MemoryGame(root)
root.mainloop()