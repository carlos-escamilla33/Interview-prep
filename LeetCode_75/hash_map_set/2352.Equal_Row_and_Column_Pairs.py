def rowCount(grid):
    ht = {}

    for row in range(len(grid)):
        row_tuple = tuple(grid[row])
        if row_tuple not in ht:
            ht[row_tuple] = 0
        ht[row_tuple] += 1
    
    return ht

def colCount(grid):
    ht = {}

    for col in range(len(grid[0])):
        col_arr = []
        for row in range(len(grid)):
            col_arr.append(grid[row][col])
        col_tuple = tuple(col_arr)
        if col_tuple not in ht:
            ht[col_tuple] = 0
        ht[col_tuple] += 1
    
    return ht

def equalPairs(grid):
    rowsCount = rowCount(grid)
    colsCount = colCount(grid)
    count = 0

    for row in rowsCount.keys():
        if row in colsCount:
            count += (rowsCount[row] * colsCount[row])
    
    return count