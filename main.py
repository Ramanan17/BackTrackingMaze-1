maze = []
entry = None
exit = None
# Take input
while True:

    row = input()

    # Convert rows into maze matrix 
    if "entry" not in row and "exit" not in row:
        row = list(map(lambda x: int(x), list(row)))
        maze.append(row)

    # Take entry for entry and exit
    elif "entry" in row:
        entry = eval(row.split(":")[1].strip())

    elif "exit" in row:
        exit = eval(row.split(":")[1].strip())
        break

    else:
        break


# Maze size
M, N = len(maze), len(maze[0])

# A function to print solution matrix sol
def outputSolution(sol):

    for pairs in sol:

        print(pairs)


# function to check if x, y is valid
# index for M * N Maze
def isSafe(maze, x, y):

    if x >= 0 and x < M and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False


""" Solve maze using back tracking
	It uses solveMazeBackTracking() to solve the problem. It
	returns false if no path is possible, otherwise return
	true and prints the pair of points taken as shown in the question output
	that there may be more than one solutions, this function
	prints one of the feasable solutions. """


def solveMaze(maze):

    # Create a list for stroing solution
    sol = []
    # Check if solution exists else print not solution
    entry_x, entry_y = entry
    # Check is solution exists and print the corresponding output
    if solveMazeBackTracking(maze, entry_x, entry_y, sol) == False:
        print("no solution")
        return False

    outputSolution(sol)
    return True


# A recursive utility function to solve Maze problem
def solveMazeBackTracking(maze, x, y, sol):

    # if (x, y is goal) return True
    if x == exit[0] and y == exit[1] and maze[x][y] == 1:
        sol.append((x, y))
        return True

    # Check if maze[x][y] is valid
    if isSafe(maze, x, y) == True:
        # Check if the current block is already part of solution path.
        if (x, y) in sol:
            return False

        # mark x, y as part of solution path
        sol.append((x, y))

        # Move forward in x direction
        if solveMazeBackTracking(maze, x + 1, y, sol) == True:
            return True

        # If moving in x direction doesn't give solution
        # then Move down in y direction
        if solveMazeBackTracking(maze, x, y + 1, sol) == True:
            return True

        # If moving in y direction doesn't give solution then
        # Move back in x direction
        if solveMazeBackTracking(maze, x - 1, y, sol) == True:
            return True

        # If moving in backwards in x direction doesn't give solution
        # then Move upwards in y direction
        if solveMazeBackTracking(maze, x, y - 1, sol) == True:
            return True

        # If none of the above movements work then
        # unmark x, y as part of solution path
        sol[x][y] = 0
        return False


solveMaze(maze)
