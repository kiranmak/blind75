'''
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dp(src, dst, memo):
            if (src,dst) in memo: return memo[(src,dst)]
            if dst == len(text2) or src == len(text1): return 0

            if text1[src] == text2[dst]:
                length = 1 + dp(src+1, dst+1, memo)
            else:
                x = dp(src+1, dst, memo)
                y = dp(src, dst+1, memo)
                length = max(x, y)
            memo[(src,dst)] = length
            return length

        m = len(text1)
        n = len(text2)
        dp2 = [[-1] * n for _ in range(m)]

        def lcs(i, j):
            if i >= m or j >= n: return 0
            if dp2[i][j] != -1:
                return dp2[i][j]
            if text1[i] == text2[j]:
                dp2[i][j] = 1 + lcs(i+1, j+1)
            else:
                dp2[i][j] = max(lcs(i+1, j), lcs(i, j+ 1))
            return dp2[i][j]

        #memo = {}
        #maxL = dp(0,0, memo)
        #return maxL
        return lcs(0,0)
            
text1, text2 = "abcde", "ace"
s = Solution()
print(s.longestCommonSubsequence(text1, text2)) # --> 3
print(s.longestCommonSubsequence("ezupkr", "ubmrapg")) # --> 2