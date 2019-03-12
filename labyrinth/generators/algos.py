from labyrinth.generators import (binary_tree, aldous_broder, recursive_backtracker,
                                  sidewinder, hunt_and_kill, prim, recursive_division)


algo_list = {
    "binary_tree" : binary_tree.BinaryTree,
    "backtracker": recursive_backtracker.RecursiveBacktracker,
    "aldous_broder": aldous_broder.AldousBroder,
    "sidewinder": sidewinder.Sidewinder,
    "hunt_and_kill" : hunt_and_kill.HuntAndKill,
    "prims": prim.Prim,
    "recursive_division": recursive_division.RecursiveDivision
}