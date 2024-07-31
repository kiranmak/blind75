'''
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counter = defaultdict(list)
        
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c)- ord('a')] += 1
            # cant use list as key directly
            counter[tuple(key)].append(s)

        return counter.values()
                    
    
s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
#strs = ["eat", "tan", "tea"]
print(strs)
output = s.groupAnagrams(strs)
for o in output:
    print(o)