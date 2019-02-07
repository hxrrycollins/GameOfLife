'''We assume a 'live' cell is denoted with a 1, and a 'dead' cell is denoted with a 0.
Taking into account that 'infinite' cannot be made, I have written the program such that
when a cell is examined by user choice, the grid will grow if none-existent cells are examined -- assumed all cells outside of initial seed grid are 'dead'
The program starts with a 5x5 seed grid. User may enter (x,y) where 0 <= x,y <= 4 (in initial grid) to reevaluate life of cell
Run in terminal/Python3'''

grid = [[0,1,1,0,0],[1,1,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,1,1,1]]
run_check=True

def evaluate_life(x, y):
    print_grid()
    counter = 0
    lessX = False
    lessY = False

    if y-1<0:
        grid.insert(0, ([0]*len(grid[0])))
        y=y+1

    if x-1<0:
        for row in grid:
            row.insert(0,0)
        x=x+1

    for i in range(y-1,y+2):
        for j in range(x-1,x+2):


            try:
                row = grid[i]
            except IndexError:
                grid.append([0]*len(grid[i-1]))
            try:
                column = grid[i][j]
            except IndexError:
                for row in grid:
                    row.append(0)

            if(grid[i][j]==1):
                counter=counter+1


    if grid[y][x]==1:
        if counter<2:
            grid[y][x]=0
        elif counter>3:
            grid[y][x]=0

    else:
        if(counter==3):
            grid[y][x]=1

def print_grid():
    for i in range(len(grid)-1, -1, -1):
        print(' '.join(map(str,grid[i])))



while(run_check):
    run_check = input("Enter R to run or Q to quit: ")

    if run_check == 'Q':
        run_check=False

    else:
        x_coord = int(input("Enter X coordinate: "))
        y_coord = int(input("Enter Y coordinate: "))
        evaluate_life(x_coord,y_coord)
        print("")
        print_grid()
        print("")



print(" ")
