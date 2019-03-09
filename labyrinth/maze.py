#! /usr/bin/env python3
import argparse

from PIL import Image, ImageDraw

from labyrinth.generators.algos import algo_list

def is_greater_than_one(val):
    value = int(val)
    if value <= 1:
        raise argparse.ArgumentTypeError("Must be greater than one.")
    return value

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rows", type = is_greater_than_one,
                        default = 20, help = "number of rows in the maze")
    parser.add_argument("-c", "--cols", type = is_greater_than_one,
                        default = 20, help = "number of cols in the maze")
    parser.add_argument("generator", type = str, choices = algo_list.keys(),
                        help = "specify the generation algorithm")
    args = parser.parse_args()

    rows = args.rows
    cols = args.cols
    generator = args.generator

    maze = algo_list[generator](rows,cols).gen_maze()

    im = Image.new("RGB", (cols*20, rows*20), (255,255,255,0))
    draw = ImageDraw.Draw(im)
    for i in range(rows):
        for j in range(cols):
            x = j*20
            y = i*20
            if maze[i][j].walls["S"]:
                draw.line([(x, y + 20), (x + 20, y + 20)], fill = (0,0,0,0))
            if maze[i][j].walls["E"]:
                draw.line([(x + 20, y), (x + 20, y + 20)], fill = (0,0,0,0))
    im.show()