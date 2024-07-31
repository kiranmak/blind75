'''
76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''
import sys
class Solution:
    def minWindowNoDups(self, s: str, t: str) -> str:
        t_dist = {}
        min_dist = sys.maxsize
        ans = []

        if s == "" or s < t:
            return ""
        
        for i in range(len(s)):
            for tt in t :
                if s[i] == tt:
                    t_dist[tt] = i

            if len(t_dist) < len(t):
                continue
            # potential ans
            mx = max(t_dist, key=t_dist.get)
            mn = min(t_dist, key=t_dist.get)
            dist = t_dist[mx] - t_dist[mn]
            print("mx=", t_dist[mx], "mn=", t_dist[mn], "dist", dist, "t_dist", t_dist)
            if min_dist > dist:
                min_dist = dist
                ans = [t_dist[mx], t_dist[mn]]

        if min_dist == sys.maxsize:
            return ""
        if ans[0] > ans[1]:
            return s[ans[1]:ans[0]+1]
        else:
            return s[ans[0]:ans[1]+1]

    def minWindow(self, s: str, t: str) -> str:
        t_win, s_win = {}, {}
        t_win_cnt,s_win_cnt = 0, 0
        l, ans = 0, [-1, -1]
        res_len = sys.maxsize

        if s == "": return ""
        
        for tt in t :
            t_win[tt] = t_win.get(tt, 0) + 1
        t_win_cnt = len(t_win)

        for r, c in enumerate(s):
            if c in t_win:
                s_win[c] = s_win.get(c, 0) + 1
                if s_win[c] == t_win[c]:
                    s_win_cnt += 1

            while s_win_cnt == t_win_cnt:
                if res_len > (r -l +1):
                    ans = [l, r]
                    res_len = r - l + 1
                
                if s[l] in t_win:
                    s_win[s[l]] -= 1
                    if s_win[s[l]] < t_win[s[l]]:
                        s_win_cnt -= 1
                l += 1
        if res_len == sys.maxsize:
            return ""
        elif ans[0] == ans[1]:
            return s[0]
        else:
            return s[ans[0]:ans[1]+1]
                
s = Solution()

#input, t = "ADOBECODEBANC", "ABC"
#input, t = "a", "a"
input, t = "aba", "aa"
input, t = "ab", "b"
ans = s.minWindow(input, t)
print(ans) 
            