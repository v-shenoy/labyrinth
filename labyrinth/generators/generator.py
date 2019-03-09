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
        pass
        
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