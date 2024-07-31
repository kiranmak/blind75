"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring
 without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
#import sys
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mydict = {}
        longest, i, ss = 0, 0, ""

        while i < len(s):
            if s[i] in mydict:
                longest = max(longest, len(ss))
                j = 0
                while ss[j] != s[i]:
                    mydict.pop(ss[j])
                    j+=1
                ss = ss[j+1:]

            ss += s[i]
            mydict[s[i]] = True
            i += 1
        return max(longest, len(ss))

    
lst = []
lst += ["abcabcbb"]
lst += ["bbbbb"]
lst += ["pwwkew"]
lst += [" "]
sol = Solution()

for test_str in lst:
    mlen = sol.lengthOfLongestSubstring(s=test_str)
    print("len", mlen)
    