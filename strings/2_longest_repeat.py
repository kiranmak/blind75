"""
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
r=A,s=0
AAB
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
      0 1 2 3 4 5 6 7 8 9  
ss = "A B B B C B B B A B"
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxFreq = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])
            if r - l + 1- maxFreq > k:
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1
        return max(maxFreq, r - l+1) 

s = Solution()
ss = "ABBBCBBBAB"
#ss = "AAAB"
output = s.characterReplacement(ss, k=0)
print(output)
output = s.characterReplacement(ss, k=1)
print(output)
output = s.characterReplacement(ss, k=2)
print(output)

