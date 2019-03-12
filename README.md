# Labyrinth
---

Labyrinth is a maze generating tool written in Python for visualizing different generation algorithms. It generates a png file for the maze, and a gif of the generation process.

Current algorithms that are implemented -
1. Binary Tree
2. Aldous Broder
3. Recursive Backtracking
4. Sidewinder
5. Hunt & Kill
6. Prims
7. Recursive Division

# Requirements
1. Python3
2. Libaries - Pillow, imageio 
3. External - Gifsicle

# Setting Up
Labyrinth uses gifsicle to optimize the generated gifs by imageio. It also uses gifview a built-in utility of gifsicle to display the gif after execution. 
After cloning the repositroy install gifsicle using the instructions for your system's packaging manager.
### Installing Gifsicle -

#### For Ubuntu -
```
$ sudo apt-get update && sudo apt-get install gifsicle
```
#### Arch-based distros
```
$ sudo pacman -Syu gifsicle
```
### Libraries
```
$ pip install -r requirements.txt
```
### Usage
``` 
$ python labyrinth.py -h
usage: labyrinth.py [-h] [-r ROWS] [-c COLS] [-s SAVE]
                    {binary_tree,backtracker,aldous_broder,sidewinder,hunt_and_kill,prims,recursive_division}
```
Labyrinth takes one positional arguments, the generating algorithm to be used. Optional flags can be used to set custom width and height for the maze. The default size is a 20x20 grid. Another optional flag -s can be used to specify the file name to save the image & gif with ("temp is used by default").  
Example -
```
$ python labyrinth.py recursive_backtracker -s backtracker
```
# Note
I implemented the algorithms a day before my exams, and my only focus was getting them to work. An effect of this is, the implementations are very naive making them slow. The gif is also built in memory by copying images frame by frame which can lead to high memory usage on bigger grids (especially on the slower algorithms such as Aldous Broder, Hunt & Kill).

If you want to improve upon it, there are various optimizations that could be done.
Instead of using Pythonic objects and lists, numpy arrays could be used for storing the maze. The information about the grid can then be stored using bit masks. 
You could possibly run the animation using matplotlib instead of building the gif. 

 ##### Well, I guess that's it. Have fun messing around. 
