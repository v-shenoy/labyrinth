#! /usr/bin/env python3
import argparse
import os

import imageio

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
    parser.add_argument("-s", "--save", type = str,
                        default = "temp", help = "specify name for saving")
    args = parser.parse_args()

    rows = args.rows
    cols = args.cols
    generator = args.generator
    name = args.save

    images = algo_list[generator](rows,cols).gen_maze()
    fps = (20 if generator == "recursive_division" else 30)
    imageio.mimsave(name + '.gif', images, fps = fps)
    imageio.imsave(name + '.png', images[-1])

    os.system("gifsicle -O3 {}.gif -o {}.gif".format(name, name))
    os.system("gifview -a {}.gif".format(name))