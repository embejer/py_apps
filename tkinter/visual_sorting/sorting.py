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
        self.root = root

        buttons = self.grid_slaves()
        for button in buttons:
            button.destroy()
            self.update()
        self.random_numbers = self.generate_random_numbers()
        self.original = self.random_numbers
        print(self.random_numbers)
        self.layout_random_numbers()
        self.layout_sort_options()        


    def generate_random_numbers(self) -> List:
        random_list = []
        for i in range(20):
            while True:
                a = random.randint(1, 100)
                if a not in random_list:
                    random_list.append(a)
                    break
        return random_list
    
    def layout_sort_options(self) -> None:
        btn_bubble = tk.Button(width=4, height=3, command=partial(self.bubble_sort, self.random_numbers))
        btn_bubble.config(state=tk.NORMAL, text=f'Bubble', foreground='black', background='tomato')
        btn_bubble.grid(row=1, column=0)
        self.update()
        btn_insert = tk.Button(width=4, height=3, command=partial(self.insert_sort, self.random_numbers))
        btn_insert.config(state=tk.NORMAL, text=f'Insert', foreground='black', background='skyblue')
        btn_insert.grid(row=1, column=1)
        self.update()
        btn_merge = tk.Button(width=4, height=3, command=partial(self.merge_sort, self.random_numbers))
        btn_merge.config(state=tk.NORMAL, text=f'Merge', foreground='black', background='lightgreen')
        btn_merge.grid(row=1, column=2)
        self.update()
        btn_merge = tk.Button(width=4, height=3, command=self.quick_sort_main)
        btn_merge.config(state=tk.NORMAL, text=f'Quick', foreground='black', background='lightyellow')
        btn_merge.grid(row=1, column=3)
        self.update()

        btn_merge = tk.Button(width=4, height=3, command=partial(self.__init__, self.root))
        btn_merge.config(state=tk.NORMAL, text=f'Reset', foreground='black', background='pink')
        btn_merge.grid(row=1, column=19)
        self.update()

    def layout_random_numbers(self, numbers: List=None) -> None:
        for idx, num in enumerate(self.random_numbers):
            button = tk.Button(width=4, height=3)
            if numbers and num in numbers:
                button.config(state=tk.DISABLED, text=f'{num}', disabledforeground='black', background='tomato')
            else:
                button.config(state=tk.DISABLED, text=f'{num}', disabledforeground='black')
            button.grid(row=0, column=idx)
            self.update()
        numbers = None

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:

                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
                self.layout_random_numbers([array[i], array[j]])
                print(array)

        (array[i + 1], array[high]) = (array[high], array[i + 1])
        self.layout_random_numbers([array[i + 1], array[high]])
        print(array)
        return i + 1
    
    def quick_sort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quick_sort(array, low, pi - 1)
            self.quick_sort(array, pi + 1, high)

    def quick_sort_main(self, numbers: List=None) -> None:
        size = len(self.random_numbers)
        self.quick_sort(self.random_numbers, 0, size-1)
        print(self.random_numbers)
        
    def bubble_sort(self, numbers: List) -> None:
        ll = len(numbers)
        for x in range(ll):
            for y in range(x+1, ll):
                if numbers[y] < numbers[x]:
                    numbers[y], numbers[x] = numbers[x], numbers[y]
                    self.layout_random_numbers([numbers[x], numbers[y]])
                    print(f'Bubble Sorting => ', numbers)

    
    def insert_sort(self, numbers: List) -> None:
        ll = len(numbers)
        for x in range(ll):
            y = x
            while y > 0 and numbers[y-1] > numbers[y]:
                numbers[y], numbers[y-1] = numbers[y-1], numbers[y]
                self.layout_random_numbers([numbers[y-1], numbers[y]])
                print(f'Insertion Sorting => ', numbers)
                y -= 1

    def merge_sort(self, numbers: List) -> None:
        ll = len(numbers)
        if ll > 1:
            l = numbers[:ll//2]
            r = numbers[ll//2:]

            self.merge_sort(l)
            self.layout_random_numbers(l)
            self.merge_sort(r)
            self.layout_random_numbers(r)
        
            a = 0
            b = 0
            '''new merge index'''
            c = 0

            while a < len(l) and b < len(r):  
                temp_list = l + r
                print('Merge Sorting', temp_list)
                self.layout_random_numbers(temp_list)
                if l[a] < r[b]:
                    numbers[c] = l[a]
                    old_value = self.random_numbers[c]
                    old_index = self.random_numbers.index(l[a])
                    self.random_numbers[c] = l[a]
                    self.random_numbers[old_index] = old_value
                    a += 1
                else:
                    numbers[c] = r[b]
                    old_value = self.random_numbers[c]
                    old_index = self.random_numbers.index(r[b])
                    self.random_numbers[c] = r[b]
                    self.random_numbers[old_index] = old_value
                    b += 1
                c += 1
        
            while a < len(l):
                numbers[c] = l[a]
                old_value = self.random_numbers[c]
                old_index = self.random_numbers.index(l[a])
                self.random_numbers[c] = l[a]
                self.random_numbers[old_index] = old_value
                self.layout_random_numbers([l[a], old_value])
                print('Merge Sorting', [l[a], old_value])
                a += 1
                c += 1
                
            while b < len(r):
                numbers[c] = r[b]     
                old_value = self.random_numbers[c]
                old_index = self.random_numbers.index(r[b])
                self.random_numbers[c] = r[b]
                self.random_numbers[old_index] = old_value 
                self.layout_random_numbers([r[b], old_value])
                print('Merge Sorting', [r[b], old_value])
                b += 1
                c += 1


root = tk.Tk()
root.eval('tk::PlaceWindow . center')
myapp = App(root)
myapp.master.title = 'Merge Sort Visualization'
myapp.mainloop()