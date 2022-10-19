# Problem:
# You are given a 2D matrix containing only 1s (land) and 0s (water).
# Two islands are considered the same if they can be translated (not rotated/reflected) to equal each other. 

# Write a function to find the number of distinct islands in the given matrix

# This question is similar to number of islands. We will traverse the matrix linearly to find islands. We
# can use DFS to traverse the islands and find all connecting land cells.

# If two islands are same, their traversal path should be same too. This means, if we perform a DFS or BFS on
# two equal islands starting from their top-left cell, the traversal pattern should be exactly same for both the
# islands

# We can start inserting these traversal strings of each island in a HashSet. This will ensure that we will not
# have any duplicate traversal string in the HashSet, thus giving us distinct islands. When we finish traversing
# the matrix, the HashSet will contain the distinct traversal path of all islands. Hence, the total number of
# elements in the HashSet will be equal to distinct number of islands

# Time Complexity: O(M*N)
# The time complexity will be O(M*N) where M is the number of rows and N is the number of columns in the matrix

# Space Complexity: O(M*N)
# The DFS stack can go up to M*N deep when the entire matrix is filled with 1. Thus, the space complexity is
# O(M*N) where M is the number of rows and N is the number of columns

def findDistinctIslands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for c in range(cols)] for r in range(rows)]
    islandSet = set()

    for r in range(rows):
        for c in range(cols):
            # if the cell is land and not visited
            if matrix[r][c] == 1 and not visited[r][c]:
                islandSet.add(dfs(matrix, visited, r, c, "O")) # "O" for origin
    
    return len(islandSet)

def dfs(matrix, visited, r, c, direction):
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
        return "" # return if not valid cell
    
    if matrix[r][c] == 0 or visited[r][c]:
        return "" # return if water cell or visited

    visited[r][c] = True # mark cell as visited
    islandTraversal = direction
    # recursively visit all neighboring cells
    islandTraversal += dfs(matrix, visited, r + 1, c, "D")
    islandTraversal += dfs(matrix, visited, r - 1, c, "U")
    islandTraversal += dfs(matrix, visited, r, c + 1, "R")
    islandTraversal += dfs(matrix, visited, r, c - 1, "L")

    islandTraversal += "E" # "E" for end

    return islandTraversal

def main():
    print(findDistinctIslands([[1, 1, 0, 1, 1],
                               [1, 1, 0, 1, 1],
                               [0, 0, 0, 0, 0],
                               [0, 1, 1, 0, 1],
                               [0, 1, 1, 0, 1]]))

    print(findDistinctIslands([[1, 1, 0, 1],
                               [0, 1, 1, 0],
                               [0, 0, 0, 0],
                               [1, 1, 0, 0],
                               [0, 1, 1, 0]]))
  
main()