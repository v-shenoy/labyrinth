class Cell:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = {"N": True, "E": True, "S": True, "W": True}
        self.vis = False