import random

from labyrinth.generators.generator import Generator

class Prim(Generator):

    def __init__(self, rows, cols):
        super(Prim, self).__init__(rows, cols)

    def gen_maze(self):
        super().gen_maze()
        cells = []        
        i = random.randint(0, self.rows - 1)
        j = random.randint(0, self.cols - 1)

        start = self.grid[i][j]
        self.add_to_list(cells, start)
        while cells:
            cell = random.choice(cells)
            walls = ["N", "E", "S", "W"]
            random.shuffle(walls)
            remove = True
            for wall in walls:
                if self.is_safe(wall, cell.row, cell.col):
                    neighbour = self.get_neighbour(wall, cell.row, cell.col)
                    if not neighbour.vis:
                        self.link(wall, cell.row, cell.col)
                        self.add_to_list(cells, neighbour)
                        remove = False
                        break
            if remove:
                self.remove(cells, cell)
        return self.images

    def add_to_list(self, cells, cell):
        cells.append(cell)
        cell.vis = True
        cell.color = (239, 158, 158, 255)
        self.draw(cell)

    def remove(self, cells, cell):
        cells.remove(cell)
        cell.color = (255, 255, 255, 255)
        self.draw(cell)