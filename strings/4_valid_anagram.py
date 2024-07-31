"""
Given two strings s and t, return true if t is an anagram of s, and
false otherwise.
An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters
exactly once.
Input: s = "anagram", t = "nagaram"
Output: true
Input: s = "rat", t = "car"
Output: false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        if s == "" and t == "":
            return True
        
        if s == "" or t == "":
            return False

        for c in s:
            s_map[c] = 1 + s_map.get(c, 0)
        
        for c in t:
            if c not in s_map:
                return False
            s_map[c] -= 1
            if s_map[c] == 0:
                s_map.pop(c)

        
        if len(s_map) == 0:
            return True
        else: return False