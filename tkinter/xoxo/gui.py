from functools import partial
import tkinter.font as tkFont
from tkinter import messagebox 
from typing import List
import tkinter as tk
import random
import time

class App(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.initialize()

    def initialize(self) -> None:
        self.fontObj = tkFont.Font(size=18)
        self.human_slope_count = 0
        self.ai_slope_count = 0
        self.human_positions = set()
        self.ai_positions = set()

        self.create_boxes()

    def create_boxes(self) -> None:
        for y in range(3):
            for x in range(3):
                self.button = tk.Button(width=10, height=5, font=('Monospace', 18, 'bold'), \
                    command=partial(self.human_check_coordinates, self.human_positions, (y, x))) 
                self.button['text'] = f'({y},{x})'
                self.button.grid(row=y, column=x)
        self.for_x = tk.Button(width=4, height=2, command=self.initialize) 
        self.for_x.grid(row=4, column=2)
        self.for_x.config(bg='tomato', font=self.fontObj)
        self.for_x['text'] = 'clear'

    def human_check_coordinates(self, s_list: set, coor: tuple) -> None:
        while True:
            try:
                s_list.add(coor)
                self.button = tk.Button(width=10, height=5, font=('Monospace', 18, 'bold')) 
                self.button['text'] = 'X'
                self.button.config(bg='tomato')
                self.button.grid(row=coor[0], column=coor[1])
                self.button['state'] = 'disabled'
                self.update()
                time.sleep(0.2)
                if self.validator(s_list, 'Human'):
                    break
                self.ai_check_coordinates()
                return
            except:
                continue

    def ai_check_coordinates(self):
         while True:
            try:
                y, x = self.get_ai_coordinates()
                self.ai_positions.add((y, x))
                self.button = tk.Button(width=10, height=5, font=('Monospace', 18, 'bold')) 
                self.button['text'] = 'O'
                self.button.config(bg='limegreen')
                self.button.grid(row=y, column=x)
                self.button['state'] = 'disabled'
                self.update()
                time.sleep(0.2)
                self.validator(self.ai_positions, 'AI')
                return
            except:
                continue

    def validator(self, s_list: set, type: str):
        if s_list:
            if self.check_winner(s_list):
                messagebox.showinfo(f'Result', message=f'{type} Wins !!!')
                self.initialize()
                return True
        if len(s_list) == 5:
            messagebox.showinfo(f'Result', message='No Winner !!!')
            self.initialize()
            return True

    def check_winner(self, s_set: set):
        for y in range(3):
            if (y, 0) in s_set and (y, 1) in s_set and (y, 2) in s_set:
                return True
        for x in range(3):
            if (0, x) in s_set and (1, x) in s_set and (2, x) in s_set:
                return True            
        if (2, 0) in s_set and (1, 1) in s_set and (0, 2) in s_set:
            return True
        if (0, 0) in s_set and (1, 1) in s_set and (2, 2) in s_set:
            return True
        return False

    def get_ai_coordinates(self):
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if (y, x) not in self.human_positions and (y, x) not in self.ai_positions:
                return (y, x)
            
    
root = tk.Tk()
root.eval('tk::PlaceWindow . center')
myapp = App(root)
myapp.master.title("My XOXO Application")
myapp.mainloop()