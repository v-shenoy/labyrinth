import random
import sys

from labyrinth.generators.generator import Generator

class RecursiveBacktracker(Generator):

    def __init__(self, rows, cols):
        super(RecursiveBacktracker, self).__init__(rows, cols)

    def gen_maze(self):
        sys.setrecursionlimit(1000000)
        i = random.randint(0, self.rows - 1)
        j = random.randint(0, self.cols - 1)

        source = self.grid[i][j]
        self.dfs(source)
        return self.grid

    def dfs(self, curr):
        if curr.vis:
            return
        
        curr.vis = True
        walls = ["N", "E", "S", "W"]
        random.shuffle(walls)

        for wall in walls:
            if self.is_safe(wall, curr.row, curr.col):
                neighbour = self.get_neighbour(wall, curr.row, curr.col)
                if not neighbour.vis:
                    self.link(wall, curr.row, curr.col)
                    self.dfs(neighbour)