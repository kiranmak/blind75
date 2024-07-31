'''
5. Longest Palindromic Substring
Given a string s, return the longest 
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return s
            
        ans = s[0] 
        ansLen = 1
        
        for i in range(len(s)):
            l, r = i - 1, i + 1
            ans, ansLen = self.check(s, l, r, ansLen, ans)

            l, r = i, i + 1
            ans, ansLen = self.check(s, l, r, ansLen, ans)

        return ans

    def check(self, s, l, r, ansLen, ans):
        orig = r - l
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l, r = l - 1, r + 1
            else:
                break
        if orig < r - l and ansLen < r -1 - (l+1) + 1:
            ansLen = r -1 -(l + 1) + 1
            ans = s[l+1: r]
        return ans, ansLen
        

input = "babad"   #odd palen
#input = "dcbbd"  #even
input = "aa"
s = Solution()
ans = s.longestPalindrome(input)
print("string:", input, "ans: ", ans)