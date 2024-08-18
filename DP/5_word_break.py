'''
139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        visited = [False] * len(wordDict)
        
        def match(word):
            for j in range(len(wordDict)):
                if visited[j]: continue
                sz = len(wordDict[j])
                if word[:sz] == wordDict[j]:
                    visited[j] = True
                    return word[sz:]
            return []
            
        def tmp(word):
            if len(word) == 0: return  True

            suffix = match(word)

            if len(suffix) == len(word):
                print(f"word:{word}, suf={suffix}: res - not found")
                return False
            elif len(suffix) == 0 and len(word):
                print(f"word:{word}, suf={suffix}: done")
                return False
            else:
                print(f"word:{word}, suf={suffix}: res - recurse")
                return tmp(suffix)
        
        result = tmp(s)
        return result

s = Solution()
print(s.wordBreak("codeleet", ["leet", "code"]))            
print(s.wordBreak("catsandog",["cats","dog","sand","and","cat"]))