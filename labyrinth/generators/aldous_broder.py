import random

from labyrinth.generators.generator import Generator

class AldousBroder(Generator):

    def __init__(self, rows, cols):
        super(AldousBroder, self).__init__(rows, cols)

    def gen_maze(self):
        i = random.randint(0, self.rows - 1)
        j = random.randint(0, self.cols - 1)

        curr = self.grid[i][j]
        curr.vis = True
        remaining = self.rows*self.cols - 1
        while remaining > 0:
            walls = ["N", "E", "S", "W"]
            random.shuffle(walls)
            for wall in walls:
                if self.is_safe(wall, curr.row, curr.col):
                    neighbour = self.get_neighbour(wall, curr.row, curr.col)
                    if neighbour.vis == False:
                        self.link(wall, curr.row, curr.col)
                        neighbour.vis = True
                        remaining = remaining - 1
                    curr = neighbour
                    break

        return self.grid