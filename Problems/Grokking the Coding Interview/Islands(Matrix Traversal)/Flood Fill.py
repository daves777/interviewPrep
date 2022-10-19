# Problem:
# Flood fill algorithm takes a starting cell (i.e., a pixel) and a color. The given color is applied to all
# horizontally and vertically connected cells with the same color as that of the starting cell. Recursively,
# the algorithm fills cells with the new color until it encounters a cell with a different color than the
# starting cell. Given a matrix, a starting cell, and a color, flood fill the matrix.

# This question is similar to Number of Islands
# From the starting cell, we can perform a Depth First Search (DFS) to find all connected cells with the same
# color. During the DFS traversal, we'll update the cells with the new color

# Time Complexity: O(M*N)
# The time complexity will be O(M*N) where M is the number of rows and N is the number of columns in the matrix

# Space Complexity: O(M*N)
# The DFS stack can go up to M*N deep when the entire matrix is filled with 1. Thus, the space complexity is
# O(M*N) where M is the number of rows and N is the number of columns

def floodFill(matrix, x, y, newColor):
    if matrix[x][y] != newColor: # If selected cell is different from the desired color, perform DFS
        fillDFS(matrix, x, y, matrix[x][y], newColor)
    return matrix

def fillDFS(matrix, x, y, oldColor, newColor):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]): # if cell out of bounds
        return
    if matrix[x][y] != oldColor: # if not the old color
        return
    matrix[x][y] = newColor # update cell to new color

    # Recusively visit all neighboring cells
    fillDFS(matrix, x + 1, y, oldColor, newColor) # lower cell
    fillDFS(matrix, x - 1, y, oldColor, newColor) # upper cell
    fillDFS(matrix, x, y + 1, oldColor, newColor) # right cell
    fillDFS(matrix, x, y - 1, oldColor, newColor) # left cell


def main():
    print(floodFill([[0, 1, 1, 1, 0],
                     [0, 0, 0, 1, 1],
                     [0, 1, 1, 1, 0],
                     [0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0]], 1, 3, 2))

    print(floodFill([[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0]], 3, 2, 5))


main()