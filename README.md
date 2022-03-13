# Maze Solver
Python script for solving text based mazes.

Instead of calculating every point in the queue, this script gives priority to nearest points and saves time.

## Usage
maze.py script
1. takes a text file that contains maze data,
2. solves it,
3. writes the solution to output file.

### Basic
```python3 maze.py```
Uses default values below.

Input file: ```maze.txt``` 

Output file: ```maze-solved.txt```

Move limit: ```5000```

### Specify input and output file
```python3 maze.py maze.txt maze-solved.txt```

### Specify input file, output file and move limit
```python3 maze.py maze.txt maze-solved.txt 10_000```

## Input and Output Data
**#**: Wall

**S**: Starting point

**T**: Target point

*spaces*: Spaces.

*numbers*: Solution path. Repeating cycle of numbers: [0-9].

*dots*: Calculated but neglected points.

**X**: Blocked point. Cannot move forward. Turns into dot after solution.

**O**: Prepending point. Waiting to be calculated. Turns into dot after solution.

### Sample Input File
```
###########
#S        #
#         #
###### ####
#T        #
###########
```

### Sample Output File for a Solved Maze
```
###########
#S.....   #
#012345.  #
######6####
#T10987.  #
###########
```

### Sample Output File for an Unsolved Maze
```
###########
#SXO      #
#XXXO     #
###### ####
#T        #
###########
```