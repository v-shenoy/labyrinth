import random
import sys

from labyrinth.generators.generator import Generator

class HuntAndKill(Generator):

    def __init__(self, rows, cols):
        super(HuntAndKill, self).__init__(rows, cols)

    def gen_maze(self):
        super().gen_maze()
        sys.setrecursionlimit(1000000)
        x = random.randint(0, self.rows - 1)
        y = random.randint(0, self.cols - 1)
        
        source = self.grid[x][y]
        self.remaining = self.rows * self.cols
        self.dfs(source)
        while self.remaining > 0:
            self.hunt()                    
        return self.images

    def hunt(self):
        for i in range(self.rows):
            for j in range(self.cols):
                curr = self.grid[i][j]
                if curr.vis:
                    continue
                temp = curr.color
                curr.color = (187, 252, 146, 255)
                self.draw(curr)
                walls = ["N", "E", "S", "W"]
                random.shuffle(walls)
                for wall in walls:
                    if self.is_safe(wall, curr.row, curr.col):
                        neighbour = self.get_neighbour(wall, curr.row, curr.col)
                        if neighbour.vis:
                            self.link(wall, curr.row, curr.col)
                            self.dfs(curr)   
                            return
                curr.color = temp
                self.draw(curr)

    def dfs(self, curr):
        if curr.vis:
            return
        
        curr.vis = True
        self.remaining -= 1
        curr.color = (239, 158, 158, 255)
        self.draw(curr)
        walls = ["N", "E", "S", "W"]
        random.shuffle(walls)

        for wall in walls:
            if self.is_safe(wall, curr.row, curr.col):
                neighbour = self.get_neighbour(wall, curr.row, curr.col)
                if not neighbour.vis:
                    self.link(wall, curr.row, curr.col)
                    self.dfs(neighbour)
                    break
        curr.color = (255, 255, 255, 255)
        self.draw(curr)