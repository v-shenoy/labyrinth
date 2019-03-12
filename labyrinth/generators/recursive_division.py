import random
import sys

from PIL import Image, ImageDraw

from labyrinth.generators.generator import Generator

class RecursiveDivision(Generator):

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def gen_maze(self):
        sys.setrecursionlimit(1000000)
        self.images = []
        self.im = Image.new("RGB", (self.cols*20+1, self.rows*20+1), (255, 255, 255, 255))
        self.drawer = ImageDraw.Draw(self.im, "RGBA")
        self.divide(0, 0, self.cols, self.rows)
        return self.images

    def divide(self, x, y, width, height):

        if width < 2 or height < 2:
            return

        vertical = self.orientation(width,height)
        if vertical:
            wx = random.randint(1, width - 1)
            nx = x + wx
            self.drawer.line([(nx*20,y*20), (nx*20, (y+height)*20)], fill = (0,0,0,200))
            self.images.append(self.im.copy())
            py = random.randint(y, y + height -1)
            self.drawer.line([(nx*20,py*20), (nx*20,py*20+20)], fill = (255,255,255,255))
            self.images.append(self.im.copy())
            self.divide(x,y,wx,height)
            self.divide(nx,y,width-wx,height)
        else:
            hy = random.randint(1,height-1)
            ny = y + hy
            self.drawer.line([(x*20,ny*20), ((x+width)*20, ny*20)], fill = (0,0,0,200))
            self.images.append(self.im.copy())
            px = random.randint(x,x+width-1)
            self.drawer.line([(px*20,ny*20), (px*20+20, ny*20)], fill = (255,255,255,255))
            self.images.append(self.im.copy())
            self.divide(x,y,width,hy)
            self.divide(x,ny,width,height-hy)

    def orientation(self, width, height):
        if width < height:
            return random.choice([True, False, False, False, False])
        elif height < width:
            return random.choice([True, True, True, True, False])
        else:
            return random.choice([True, False])
            
