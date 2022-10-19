# Problem:
# You are given a 2D matrix containing different characters, you need to find if there exists any cycle consisting
# of the same character in the matrix.
# 
# A cycle is a path in the matrix that starts and ends at the same cell and has four or more cells. From a given
# cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right)
# if it has the same character value of the current cell. 

# Write a function to find if the matrix has a cycle.

# Solution:
# This question is similar to number of islands. We will traverse the matrix linearly to find islands. We
# can use DFS to traverse the islands and find all connecting land cells.

# Whenever we reach a cell that have already been visited, we can conclude that we have found a cycle. This also
# means that we need to be careful to not start traversing the parent cell and wrongly finding a cycle. That is,
# while traversing, when initiating DFS recursive calls to all the neighboring cells, we should not start a DFS
# call to the pervious cell

# Time Complexity: O(M*N)
# The time complexity will be O(M*N) where M is the number of rows and N is the number of columns in the matrix

# Space Complexity: O(M*N)
# The DFS stack can go up to M*N deep when the entire matrix is filled with 1. Thus, the space complexity is
# O(M*N) where M is the number of rows and N is the number of columns

def hasCycle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for c in range(cols)] for r in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]: # only if the cell is not visited
                return dfs(matrix, visited, matrix[r][c], r, c, -1, -1)
    
def dfs(matrix, visited, startChar, x, y, prevX, prevY):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return False # not a valid cell
    if matrix[x][y] != startChar:
        return False # different character means different island
    if visited[x][y]:
        return True # visiting an already visited cell, which means we have found a cycle

    visited[x][y] = True # mark cell as visited

    # recursively visit all neighboring cells
    if x + 1 != prevX and dfs(matrix, visited, startChar, x + 1, y, x, y): # down
        return True
    if x - 1 != prevX and dfs(matrix, visited, startChar, x - 1, y, x, y): # up
        return True
    if y + 1 != prevY and dfs(matrix, visited, startChar, x, y + 1, x, y): # right
        return True
    if y - 1 != prevY and dfs(matrix, visited, startChar, x, y - 1, x, y): # left
        return True
    
    return False # otherwise return false


def main():
    print(hasCycle([['a', 'a', 'a', 'a'],
                    ['b', 'a', 'c', 'a'],
                    ['b', 'a', 'c', 'a'],
                    ['b', 'a', 'a', 'a']]))

    print(hasCycle([['a', 'a', 'a', 'a'],
                    ['a', 'b', 'b', 'a'],
                    ['a', 'b', 'a', 'a'],
                    ['a', 'a', 'a', 'c']]))

    print(hasCycle([['a', 'b', 'e', 'b'],
                    ['b', 'b', 'b', 'b'],
                    ['b', 'c', 'c', 'd'],
                    ['c', 'c', 'd', 'd']]))


main()