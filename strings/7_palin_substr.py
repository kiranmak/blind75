
'''
647. Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
class Solution:
    def countSubstrings(self, s: str) -> str:

        if not s: return s
        ans =  []
        
        for i in range(len(s)):
            ans.append(s[i])
            l, r = i - 1, i + 1
            self.getPalin(s, l, r, ans)

            l, r = i, i + 1
            self.getPalin(s, l, r, ans)

        return ans

    def getPalin(self, s, l, r, ans):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                ans.append(s[l:r+1])
                l, r = l - 1, r + 1
            else: break
        
input = "babad"   #odd palen
#input = "dcbbd"  #even
#input = "aaa"
#input = "abc"
s = Solution()
ans = s.countSubstrings(input)
print("string:", input)
print(ans)