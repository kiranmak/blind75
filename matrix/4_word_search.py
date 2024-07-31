""" 
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

[
["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]], word = "ABCCED"
Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        trail = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                ans = set()
                result = self.helper(board, row, col, word, ans, trail)
                if result:
                    return result, ans
        return False, None
                

    
    def helper(self, board, hor, ver, word, ans, visited):

        if word is "":
            return True

        if (hor < 0 or ver < 0 or
            hor == len(board) or 
            ver == len(board[0])):
            return False

        if (hor,ver) in visited:
            return False
        
        if board[hor][ver] != word[0]:
            return False

        if board[hor][ver] == word[0]:
            ans.add((hor,ver))
        
        print(f"h={hor}, v={ver}, st={word[0]}")
        visited.add((hor, ver))
        result =\
              (self.helper(board, hor + 1, ver, word[1:], ans, visited) or
               self.helper(board, hor, ver+1, word[1:], ans, visited) or
               self.helper(board, hor, ver-1, word[1:], ans, visited)or
               self.helper(board, hor - 1, ver, word[1:], ans, visited))
        visited.remove((hor, ver))
        return result


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
#board = [["b"],["a"],["b"],["b"],["a"]]
#word = "baa"
s = Solution()
ans, path = s.exist(board, word)
print ("ans", ans)
if ans:
    print(path)