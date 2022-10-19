# Problem:
# You are given a 2D matrix containing only 1s (land) and 0s (water).
# A closed island is an island that is totally surrounded by 0s. This means all horizontally and vertically
# connected cells of a closed island are water. This also means that, by definition, a closed island can't
# touch an edge (as then the edge cells are not connected to any water cell). 

# Write a function to find the number of closed islands in the given matrix.

# This question is similar to number of islands. We will traverse the matrix linearly to find islands. We
# can use DFS to traverse the islands and find all connecting land cells.

# We can determine if an island is closed if the island does not touch an edge, and the outside boundary are
# all water cells

# Time Complexity: O(M*N)
# The time complexity will be O(M*N) where M is the number of rows and N is the number of columns in the matrix

# Space Complexity: O(M*N)
# The DFS stack can go up to M*N deep when the entire matrix is filled with 1. Thus, the space complexity is
# O(M*N) where M is the number of rows and N is the number of columns

def countClosedIslandsDFS(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]
    closedIslands = 0

    for r in range(rows):
        for c in range(cols):
            # only if the cell is a land and not visited
            if matrix[r][c] == 1 and visited[r][c] == False:
                if dfs(matrix, visited, r, c):
                    closedIslands += 1
    
    return closedIslands

def dfs(matrix, visited, r, c):
    if r < 0 or r > len(matrix) or c < 0 or c > len(matrix):
        return False # return false since island is touching an edge
    if matrix[r][c] == 0 or visited[r][c]:
        return True # return true since island is surrounded by water

    visited[r][c] = True # mark cell as visited 

    isClosed = True # if this is set to false by any neighboring cells then set to false
    # recursively visit all neighboring cells
    isClosed &= dfs(matrix, visited, r + 1, c) # lower cell
    isClosed &= dfs(matrix, visited, r - 1, c) # upper cell
    isClosed &= dfs(matrix, visited, r, c + 1) # right cell
    isClosed &= dfs(matrix, visited, r, c - 1) # left cell
    return isClosed

def main():
    print(countClosedIslandsDFS([[1, 1, 0, 0, 0],
                                 [0, 1, 0, 0, 0],
                                 [0, 0, 1, 1, 0],
                                 [0, 1, 1, 0, 0],
                                 [0, 0, 0, 0, 0]]))

    print(countClosedIslandsDFS([[0, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 1, 0],
                                 [0, 0, 0, 0]]))

main()
