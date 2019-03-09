import random

from labyrinth.generators.generator import Generator

class BinaryTree(Generator):

    def __init__(self, rows, cols):
        super(BinaryTree, self).__init__(rows, cols)

    def gen_maze(self):
        for j in range(self.cols-1):
            self.link("E", 0, j)
        for i in range(1, self.rows):
            self.link("N", i, self.cols-1)
        for i in range(1,self.rows):
            for j in range(self.cols-1):
                walls = ["N", "E"]
                wall = random.choice(walls)
                self.link(wall, i, j)
        return self.grid