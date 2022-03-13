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

Move limit: ```5_000```

### Specify Input and Output File
```
python3 maze.py [input_file] [output_file]
```
Example:
```
python3 maze.py maze.txt maze-solved.txt
```

### Specify Input File, Output File and Move Limit
```
python3 maze.py [input_file] [output_file] [move_limit]
```
Example:
```
python3 maze.py maze.txt maze-solved.txt 10_000
```

## Input and Output Data

The maze data of the input and output text files consist of these symbols.

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