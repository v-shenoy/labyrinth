import random

from labyrinth.generators.generator import Generator

class Sidewinder(Generator):

    def __init__(self, rows, cols):
        super(Sidewinder, self).__init__(rows, cols)

    def gen_maze(self):
        super().gen_maze()
        run = []
        for j in range(self.cols):
            self.add_to_run(run, self.grid[0][j])
            if j != self.cols - 1:
                self.link("E", 0, j)
            else:
                self.empty_run(run)
                run = []
        for i in range(1, self.rows):
            j = 0
            while j < self.cols:
                curr = self.grid[i][j]
                self.add_to_run(run, curr)
                go_east = random.choice([True, False])
                if not go_east or (j == self.cols - 1):
                    cell = random.choice(run)
                    self.link("N", cell.row, cell.col)
                    self.draw(cell)
                    self.empty_run(run)
                    run = []
                else:
                    self.link("E", i, j)
                j += 1

        return self.images

    def add_to_run(self, run, cell):
        cell.color = (239, 158, 158, 255)
        self.draw(cell)
        run.append(cell)

    def empty_run(self, run):
        for cell in run:
            cell.color = (255, 255, 255, 255)
            self.draw(cell)
        