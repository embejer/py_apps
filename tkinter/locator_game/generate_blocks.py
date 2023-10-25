from typing import List
import random

class Board:
    def __init__(self):
        # self.wall = '■■■'
        # self.path = '   '
        self.wall = 1
        self.path = 0
        self.height = 21
        self.width = 25
        self.no_of_blockers = self.width // 2

    def create_board(self) -> None:
        board = []
        for y in range(self.height):
            blockers = self.generate_blockers()
            row_list = []
            for x in range(self.width):
                if x == 0 or y == 0:
                    # print(self.wall, end='')
                    row_list.append(self.wall)
                elif x == (self.width - 1) or y == (self.height - 1):
                    # print(self.wall, end='')
                    row_list.append(self.wall)
                elif y%2 == 0 and x > 0 and x < (self.width - 1):
                    result = self.getx_blockers(x, blockers)
                    # print(result, end='')
                    row_list.append(result)
                else:
                    # print(self.path, end='')
                    row_list.append(self.path)
            # print('\n')
            board.append(row_list)
        return board

    def generate_blockers(self) -> str:
        blockers = []
        for x in range(self.no_of_blockers):
            while True:
                number = random.randrange(1, (self.width - 1), 1)
                if number not in blockers:
                    blockers.append(number)
                    break
        return blockers

    def getx_blockers(self, number: int, blockers: List[int]) -> str:
        if number in blockers:
            return self.wall
        else:
            return self.path

if __name__ == '__main__':
    board = Board()
    result = board.create_board()
    for x in result:
        print(''.join(x))