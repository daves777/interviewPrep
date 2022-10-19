# Problem:
# You are given a 2D matrix containing only 1s (land) and 0s (water).
# There are no lakes on the island, so the water inside the island is not connected to the water around it.
# A cell is a square with a side length of 1.. 

# The given matrix has only one island, write a function to find the perimeter of that island.

# Solution:
# This question is similar to number of islands. We will traverse the matrix linearly to find islands. We
# can use DFS to traverse the islands and find all connecting land cells.

# We can calculate the boundary of the island by checking if the side of an island cell is shared with another
# cell. If the other cell is water, we can include it in the permimeter

# Time Complexity: O(M*N)
# The time complexity will be O(M*N) where M is the number of rows and N is the number of columns in the matrix

# Space Complexity: O(M*N)
# The DFS stack can go up to M*N deep when the entire matrix is filled with 1. Thus, the space complexity is
# O(M*N) where M is the number of rows and N is the number of columns

def findIslandPerimeter(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    for r in range(rows):
        for c in range(cols):
            # only if the cell is land and not visited
            if matrix[r][c] == 1 and not visited[r][c]:
                return dfs(matrix, visited, r, c)
    
    return 0

def dfs(matrix, visited, r, c):
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
        return 1 # returning 1, since this a boundary cell initiated this DFS call
    if matrix[r][c] == 0:
        return 1 # returning 1, because of the shared side b/w a water and a land cell
    if visited[r][c]:
        return 0 # we have already taken care of this cell
    
    visited[r][c] = True # mark the cell visited

    edges = 0
    # recursively visit all neighboring cells (horizontally & vertically)
    edges += dfs(matrix, visited, r + 1, c) # lower cell
    edges += dfs(matrix, visited, r - 1, c) # upper cell
    edges += dfs(matrix, visited, r, c + 1) # right cell
    edges += dfs(matrix, visited, r, c - 1) # left cell
    return edges

def main():
    print(findIslandPerimeter([[1, 1, 0, 0, 0],
                               [0, 1, 0, 0, 0],
                               [0, 1, 0, 0, 0],
                               [0, 1, 1, 0, 0],
                               [0, 0, 0, 0, 0]]))

    print(findIslandPerimeter([[0, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 1, 0, 0],
                               [0, 1, 1, 0],
                               [0, 1, 0, 0]]))


main()