
# setting row and column indexes
n = 3
nn = n * n

class  Cell():
    """ cell class for oop version of suduko
    define  a class Cell() which has a value from 1-9
    class should have member variables of  rowidx,  colidx, bool fixedval, possiblevalues[], value
    it should know where it is in a multi-array grid of 3x3 and row 1x9
    """
    # python class constructor (equivalent)
    def __init__(self, rindex = 0, cindex=0, possible_vals = range(10)):
        self.row_index = rindex
        self.fixed = False
        self.col_index = cindex
        self.possible_vals = possible_vals
        self.fixed_val = 0
    
    def print_possible_vals(self):
        print(self.possible_vals)
   
    # magic method when print is called
    # returns id of object as unique memory address
    def __repr__(self):
        return "Cell Obj: %s" % id(self)

my_2d_arry_n4 = []
my_2d_arry_n9 = []

my_2d_arry_n4.append([1,0,0,4])
my_2d_arry_n4.append([0,2,0,0])
my_2d_arry_n4.append([0,0,3,0])
my_2d_arry_n4.append([0,0,0,0])

my_2d_arry_n9 =[[3,0,0,0,7,1,2,0,0], 
                [9,1,0,0,6,0,0,0,7], 
                [0,0,0,0,5,8,0,0,0], 
                [5,3,0,0,0,0,0,0,0], 
                [7,0,1,0,2,0,3,0,5], 
                [0,0,0,0,0,0,0,7,1], 
                [0,0,0,6,8,0,0,0,0], 
                [1,0,0,0,3,0,0,5,6], 
                [0,0,6,7,1,0,0,0,9]] 



# A Utility Function to print the Grid
def print_grid(arr):
    for r in arr:
        print( str(r))
    print (' ')


def in_column(matrix, i, v):
    """ 
    return True is v (value) is in colum index i (index) for given 2d list
    """
    print(f'index is: {i} val is {v}')
    for r in matrix:
        if r[i] == v:
            print('return True')
            return True
    print('return False')
    return False

def in_row(grid,r, v):
    print(f'in_rowidx is {r}, val is {v}')
    for i in range(0,nn):
            if grid[r][i] == v:
                print('return True')
                return True
    print('return False')
    return False

# Returns a boolean which indicates whether any assigned entry 
# within the specified 3x3 box matches the given number 
def used_in_box(arr,row,col,num): 
    r = row - row % n
    c = col - col % n

    for i in range(n): 
        for j in range(n): 
            if(arr[i+r][j+c] == num): 
                return True
    return False


# totally clunky code that only works for n = 4
def val_in_box(matrix,row,col,i):  
    print(f'val in box  row: {row}, col: {col}, index: {i}')
    
    box_idx = n

    if row < box_idx and col < 2:
        if i in matrix[0][0:2] or i in matrix[1][0:2]:
            return True          
    elif row > 1 and col < 2:
        if i in matrix[2][0:2] or i in matrix[3][0:2]:
            return True
    elif row > 1 and col > 1:
        if i in matrix[2][2:4] or i in matrix[3][2:4]:
            return True
    elif row < 2 and col > 1:
        if i in matrix[0][2:4] or i in matrix[1][2:4]:
            return True
    else:
        print('not in box')
        return False



def grid_complete(grid):
    val = 0  # 0 in any element of array indicate not complete
    for row in grid:
        if val in row:
            return False

    return True

def find_empty(grid,loc):
    for row in range(nn):
        for col in range(nn) :
          if grid[row][col] == 0:
              loc[0] = row
              loc[1] = col
              return True
    return False

def solve_grid(matrix):
###Takes a n  xn grid and solves for uniqueness using a recursive backtrack algorithm.

    loc = [0,0]  # index to next available spot in grid
    if not find_empty(matrix, loc):
        return True

    rowidx = loc[0]
    colidx = loc[1]          
  
             
    for val in range(1,nn+1): 
      if not in_row(matrix,rowidx,val) and not in_column(matrix,colidx, val) and not used_in_box(matrix,rowidx,colidx,val):
         matrix[rowidx][colidx] = val # let try to make this val work
         print('recurse solve_grid()')
         print_grid(matrix)
         if solve_grid(matrix): # time for recursion
            return True
         matrix[rowidx][colidx] = 0  # roll back to zero
         print_grid(matrix)

            
    print("BackTrack")
    print_grid(matrix)
    return False


#program starts here
if not solve_grid(my_2d_arry_n9):
    print('The Soduku1 is unsolveable')
else:
    print('Soduku solved')
    print_grid(my_2d_arry_n9)

