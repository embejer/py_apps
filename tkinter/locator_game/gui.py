from generate_blocks import Board
from functools import partial
from pynput.keyboard import Key, Listener
import tkinter as tk
import random
import time

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(padx=0, pady=0)        
        self.board = Board()

        self.board_layout = []
        self.start_coordinates = []
        self.goal_coordinates = []

        self.generate_gui_board(master)

        

    def add_start_goal(self, master):  
        self.queue = []
        self.seen_queue = []   
        self.track_path()

    def generate_gui_board(self, master):
        self.last_row = 0
        self.last_column = 0
        self.board_layout = self.board.create_board()
        self.ylen_board_layout = len(self.board_layout)
        self.xlen_board_layout = len(self.board_layout[0])
        self.seen_queue = []
        self.queue = []

        for row, column in enumerate(self.board_layout):
            for col, val in enumerate(column):
                
                self.wall = tk.Button(width=1, height=1)   
                self.wall['state'] = 'disabled'
                # self.wall['text'] = f'{row}, {col}'
                self.wall.grid(row=row, column=col)
                if val:
                    self.wall.config(bg='black', fg='white')
                else:  
                    self.wall.config(bg='white', fg='black')

                self.last_column = col + 1
                self.master.update()
            self.last_row = row + 1
            self.master.update()

        # '''1st way to get start and goal'''
        # self.start_coordinates = [self.ylen_board_layout - 2, random.randint(1, (self.xlen_board_layout - 2))]
        # self.goal_coordinates = [1, random.randint(1, (self.xlen_board_layout - 2))]

        '''2nd way to get start and goal'''
        while True:
            self.start_coordinates = [random.randint(0, self.ylen_board_layout-1), random.randint(0, self.xlen_board_layout-1)]
            _sc = self.start_coordinates
            while True:
                self.goal_coordinates = [random.randint(0, self.ylen_board_layout-1), random.randint(0, self.xlen_board_layout-1)]
                _gc = self.goal_coordinates
                _distance = self.compute_distance(_sc, _gc)
                if self.start_coordinates != self.goal_coordinates \
                        and self.start_coordinates[0] != self.goal_coordinates[0] \
                        and self.start_coordinates[1] != self.goal_coordinates[1] \
                        and _distance > (self.ylen_board_layout + self.xlen_board_layout) // 2:
                    break
            if self.board_layout[_sc[0]][_sc[1]] != 1 \
                        and self.board_layout[_gc[0]][_gc[1]] != 1:
                    break 

        self.start = tk.Button(width=1, height=1)   
        self.start.config(bg='yellowgreen')
        self.start.grid(row=self.start_coordinates[0], column=self.start_coordinates[1])
        self.start['state'] = 'disabled'

        self.goal = tk.Button(width=1, height=1)   
        self.goal.config(bg='orange')
        self.goal.grid(row=self.goal_coordinates[0], column=self.goal_coordinates[1])
        self.goal['state'] = 'disabled'


        self.start = tk.Button(width=1, height=1, command=partial(self.add_start_goal, master))   
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


    def add_to_queue(self, curr_coor):
        '''Adding the TOP'''
        if curr_coor[1][0] - 1 > 0 and self.board_layout[curr_coor[1][0] - 1][curr_coor[1][1]] != 1:
            _yx = [curr_coor[1][0] - 1, curr_coor[1][1]]
            _dist = int(self.compute_distance(_yx, self.goal_coordinates))
            self.queue.append([_dist, _yx])
        '''Adding RIGHT'''
        if curr_coor[1][1] + 1 <= self.xlen_board_layout - 2 and self.board_layout[curr_coor[1][0]][curr_coor[1][1] + 1] != 1:
            _yx = [curr_coor[1][0], curr_coor[1][1] + 1]
            _dist = int(self.compute_distance(_yx, self.goal_coordinates))
            self.queue.append([_dist, _yx])
        '''Adding BOTTOM'''
        if curr_coor[1][0] + 1 <= self.ylen_board_layout - 2 and self.board_layout[curr_coor[1][0] + 1][curr_coor[1][1]] != 1:
            _yx = [curr_coor[1][0] + 1, curr_coor[1][1]]
            _dist = int(self.compute_distance(_yx, self.goal_coordinates))
            self.queue.append([_dist, _yx])
        '''Adding LEFT'''
        if curr_coor[1][1] - 1 > 0 and self.board_layout[curr_coor[1][0]][curr_coor[1][1] - 1] != 1:
            _yx = [curr_coor[1][0], curr_coor[1][1] - 1]
            _dist = int(self.compute_distance(_yx, self.goal_coordinates))
            self.queue.append([_dist, _yx])

    def compute_distance(self, curr, target):
        _distance = abs(curr[0] - target[0]) + abs(curr[1] - target[1])
        return _distance
    
    def track_path(self):

        curr_coor = [100, self.start_coordinates]

        while True:
            self.seen_queue.append(curr_coor)            
            self.add_to_queue(curr_coor)
            self.queue.sort(reverse=True)

            while curr_coor in self.seen_queue:
                curr_coor = self.queue.pop()

            if curr_coor[1] == self.goal_coordinates:
                print('found')
                return

            self.path = tk.Button(width=1, height=1)   
            self.path['state'] = 'disabled'
            self.path.config(bg='yellow')
            self.path.grid(row=curr_coor[1][0], column=curr_coor[1][1])
            self.master.update()
            time.sleep(0.1)
            

root = tk.Tk()
myapp = App(root)
myapp.master.title("My Graph Application")
myapp.mainloop()