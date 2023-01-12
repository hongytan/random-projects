sudoku = [
    [8,0,7, 0,0,0, 0,0,0],
    [0,3,1, 0,0,2, 4,0,0],
    [0,4,0, 0,0,0, 0,5,2],

    [9,6,0, 4,1,0, 8,7,0],
    [1,0,0, 7,0,3, 9,2,0],
    [0,0,4, 9,0,8, 1,0,0],

    [4,0,6, 1,0,7, 2,3,0],
    [7,5,3, 0,0,0, 0,9,1],
    [0,1,0, 0,0,6, 5,0,0],
]


def print_board(state):
    count1 = 0
    count2 = 0
    for row in state:
        count1+=1
        for col in row:
            count2 += 1
            if count2 == 3:
                print(col, end=' | ')
                count2=0
            else: print(col,end=' ')
            
        print()
        if count1 == 3:
            print()
            count1=0

def is_possible_move(x,y,n):
    row = sudoku[y]
    if n in row: return False
    col = [row[x] for row in sudoku]
    if n in col: return False
    x = 3*(x//3)
    y = 3*(y//3)
    box = [sudoku[y+j][x+i] for i in range(3) for j in range(3)]
    if n in box: return False
    return True

def solve():
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for i in range(1,10):
                    if is_possible_move(col,row,i):
                        sudoku[row][col] = i
                        solve()
                        sudoku[row][col] = 0
                return
    print_board(sudoku)

solve()