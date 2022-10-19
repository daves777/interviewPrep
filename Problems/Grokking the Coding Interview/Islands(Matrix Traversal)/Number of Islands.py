# Problem:
# Given a 2D array containing only 1s (land) and 0s (water), count the number of islands in it.
# 
# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water)
# Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# We can traverse the matrix linearly to find islands
# Whenever we find a cell with the value '1', we have found an island
# Using that cell as the root node, we will perform a Depth First Search (DFS) to find all of its connected
# land cells. During our DFS traversal, we will find and mark all the horizontally and vertically connected
# land cells. We also need to have a mechanism to mark each land cell to ensure that each land cell is visited
# only once.

# Time Complexity: O(M*N)
# The time complexity will be O(M*N) where M is the number of rows and N is the number of columns in the matrix

# Space Complexity: O(1)
# The DFS stack can go up to M*N deep when the entire matrix is filled with 1. Thus, the space complexity is
# O(M*N) where M is the number of rows and N is the number of columns

def countIslandsDFS(matrix):
    if not matrix: # if matrix is empty, return 0
        return 0
    
    rows, cols = len(matrix), len(matrix[0]) # find number of rows and columns within matrix
    islands = 0

    # Iterate through every cell in the matrix
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1: # if cell is 1, we have found an island
                dfs(matrix, r, c) # perform depth first search on cell
                islands += 1 # increase number of islands by one
    return islands

def dfs(matrix, r, c):
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix):
        return # if cell is outside the matrix, return
    if matrix[r][c] == 0:
        return # if cell is not land, return
    
    matrix[r][c] = 0 # mark the cell as visited by making it 0
    dfs(matrix, r + 1, c) # lower cell
    dfs(matrix, r - 1, c) # upper cell
    dfs(matrix, r, c + 1) # right cell
    dfs(matrix, r, c - 1) # left cell

def main():
    print(countIslandsDFS([[0, 1, 1, 1, 0],
                           [0, 0, 0, 1, 1],
                           [0, 1, 1, 1, 0],
                           [0, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0]]))

    print(countIslandsDFS([[1, 1, 1, 0, 0],
                           [0, 1, 0, 0, 1],
                           [0, 0, 1, 1, 0],
                           [0, 0, 1, 0, 0],
                           [0, 0, 1, 0, 0]]))

main()