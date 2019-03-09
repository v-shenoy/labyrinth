from labyrinth.generators import (binary_tree, aldous_broder, recursive_backtracker,
                                  sidewinder)


algo_list = {
    "binary_tree" : binary_tree.BinaryTree,
    "backtracker": recursive_backtracker.RecursiveBacktracker,
    "aldous_broder": aldous_broder.AldousBroder,
    "sidewinder": sidewinder.Sidewinder
}