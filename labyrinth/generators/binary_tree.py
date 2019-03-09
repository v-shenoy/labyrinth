import random

from labyrinth.generators.generator import Generator

class BinaryTree(Generator):

    def __init__(self, rows, cols):
        super(BinaryTree, self).__init__(rows, cols)

    def gen_maze(self):
        super().gen_maze()
        self.grid[0][self.cols-1].color = (255, 255, 255, 255)
        self.draw(self.grid[0][self.cols-1])
        for j in range(self.cols-1):
            self.link("E", 0, j)
            self.grid[0][j].color = (255, 255, 255, 255)
            self.draw(self.grid[0][j])
        for i in range(1, self.rows):
            self.link("N", i, self.cols-1)
            self.grid[i][self.cols-1].color = (255, 255, 255, 255)
            self.draw(self.grid[i][self.cols-1])
        for i in range(1,self.rows):
            for j in range(self.cols-1):
                walls = ["N", "E"]
                wall = random.choice(walls)
                self.link(wall, i, j)
                self.grid[i][j].color = (255, 255, 255, 255)
                self.draw(self.grid[i][j])
        return self.images