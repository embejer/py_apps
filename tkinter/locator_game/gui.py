from generate_blocks import Board
from functools import partial
import tkinter as tk
import random

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(padx=0, pady=0)        
        self.board = Board()

        self.board_layout = []

        self.generate_gui_board(master)

    def add_start_goal(self):
        ylen_board_layout = len(self.board_layout)
        xlen_board_layout = len(self.board_layout[0])

        self.start['state'] = 'disabled'

        start_coordinates = (ylen_board_layout - 2, random.randint(1, (xlen_board_layout - 2)))
        goad_coordinates = (1, random.randint(1, (xlen_board_layout - 2)))

        self.start = tk.Button(width=1, height=1)   
        self.start.config(bg='yellowgreen')
        self.start.grid(row=start_coordinates[0], column=start_coordinates[1])

        self.goal = tk.Button(width=1, height=1)   
        self.goal.config(bg='orange')
        self.goal.grid(row=goad_coordinates[0], column=goad_coordinates[1])

    def generate_gui_board(self, master):
        self.last_row = 0
        self.last_column = 0
        self.board_layout = self.board.create_board()

        for row, column in enumerate(self.board_layout):
            for col, val in enumerate(column):
                if val:
                    self.wall = tk.Button(width=1, height=1)   
                    self.wall.config(bg='black')
                    self.wall['state'] = 'disabled'
                    self.wall.grid(row=row, column=col)
                else:
                    self.path = tk.Button(width=1, height=1)   
                    self.path.config(bg='white')
                    self.path['state'] = 'disabled'
                    self.path.grid(row=row, column=col)

                self.last_column = col + 1
            self.last_row = row + 1


        self.start = tk.Button(width=1, height=1, command=self.add_start_goal)   
        # self.start['text'] = '   Start   '
        self.start.config(bg='green')
        self.start.grid(row=self.last_row, column=1)

        self.stop = tk.Button(width=1, height=1, command=partial(self.generate_gui_board, master))   
        # self.stop['text'] = '   Refresh   '
        self.stop.config(bg='yellow')
        self.stop.grid(row=self.last_row, column=2)

        self.close = tk.Button(width=1, height=1, command=master.destroy)   
        # self.close['text'] = '   Close   '
        self.close.config(bg='red')
        self.close.grid(row=self.last_row, column=3)

root = tk.Tk()
myapp = App(root)
myapp.master.title("My Graph Application")
myapp.mainloop()