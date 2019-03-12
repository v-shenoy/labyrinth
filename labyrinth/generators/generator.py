from PIL import Image, ImageDraw

from labyrinth.cell import Cell

class Generator:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.opposite = {"N": "S", "E": "W", "S":"N", "W":"E"}
        self.create_grid()

    def create_grid(self):
        self.grid = []
        for i in range(self.rows):
            temp = [Cell(i,j) for j in range(self.cols)]
            self.grid.append(temp)

    def gen_maze(self):
        self.images = []
        self.im = Image.new("RGB", (self.cols*20+1, self.rows*20+1), (222, 224, 226, 255))
        self.drawer = ImageDraw.Draw(self.im, "RGBA")
        for i in range(self.rows):
            for j in range(self.cols):
                x = j*20
                y = i*20
                self.drawer.line([(x, y + 20), (x + 20, y + 20)], fill = (0,0,0, 200))
                self.drawer.line([(x + 20, y), (x + 20, y + 20)], fill = (0,0,0, 200))    

    def draw(self, curr):
        x = curr.col * 20
        y = curr.row * 20
        self.drawer.rectangle([(x,y), (x + 20,y + 20)], fill = curr.color)
        if curr.walls["N"]:
            self.drawer.line([(x, y), (x + 20, y)], fill = (0,0,0, 200))
        if curr.walls["W"]:
            self.drawer.line([(x, y), (x, y + 20)], fill = (0,0,0, 200))
        if curr.walls["S"]:
            self.drawer.line([(x, y + 20), (x + 20, y + 20)], fill = (0,0,0, 200))
        if curr.walls["E"]:
            self.drawer.line([(x + 20, y), (x + 20, y + 20)], fill = (0,0,0, 200))
        self.images.append(self.im.copy())
        
    def indexable(self, row, col):
        return (0 <= row < self.rows) and (0 <= col < self.cols)

    def is_safe(self, wall, row, col):

        if wall == "N":
            return self.indexable(row - 1, col)
        elif wall == "E":
            return self.indexable(row, col + 1)
        elif wall == "S":
            return self.indexable(row + 1, col)
        elif wall == "W":
            return self.indexable(row, col - 1)

    def get_neighbour(self, wall, row, col):
        if wall == "N":
            return self.grid[row - 1][col]
        elif wall == "E":
            return self.grid[row][col + 1]
        elif wall == "S":
            return self.grid[row + 1][col]
        elif wall == "W":
            return self.grid[row][col - 1]

    def link(self, wall, row, col):
        self.grid[row][col].walls[wall] = False
        opp = self.opposite[wall]
        self.get_neighbour(wall, row, col).walls[opp] = False