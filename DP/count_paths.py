'''
     0,0
     /D \R
'''

def count_paths(grid):

    '''
    def path_helper(r, c):
        if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]):
            return 0
        
        if grid[r][c] == 'X':
            return 0
            
        if r == (len(grid) - 1) and c == (len(grid[0]) - 1):
            return 1

        x = path_helper(r, c + 1)
        y = path_helper(r+1, c)
        return (x + y)
    '''
    def path_helper(r,c, memo):
        key = str(r) + ',' + str(c)
        if key in memo: return memo[key]
        
        if grid[r][c] == 'X':
            return 0

        if r == 0 or c == 0: return 1
        
        result = path_helper(r - 1, c, memo) + path_helper(r, c - 1, memo)
        
        memo[key] = result
        return result
    
    return path_helper(len(grid) - 1, len(grid[0]) - 1, memo={})
                        
grid = [
  ["O", "O"],
  ["O", "O"],
]
count = count_paths(grid) # -> 2
print("count 2/", count)

grid = [
  ["O", "O", "X"],
  ["O", "O", "O"],
  ["O", "O", "O"],
]
count = count_paths(grid) # -> 5
print("count 5/", count)

grid = [
  ["O", "O", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "X"],
  ["X", "O", "O", "O", "O", "O"],
  ["X", "X", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "X"],
]
count = count_paths(grid) # -> 0
print("count 0/", count)
