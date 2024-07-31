'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        #paren = {'{':'}', '[':']', '(':')'}
        paren = deque()
        surplus = False
        for ch in s:
            match(ch):
                case '{' | '[' | '(':
                    paren.appendleft(ch)

                case '}':
                    if paren and paren[0] == '{':
                        paren.popleft()
                    else:
                        surplus |= True
                case ')':
                    if paren and paren[0] == '(':
                        paren.popleft()
                    else:
                        surplus |= True
                case ']':
                    if paren and paren[0] == '[':
                        paren.popleft()
                    else:
                        surplus |= True
                case _:
                    pass
                    

        print(paren)
        return False if paren or surplus else True
                

#s = "()"
#s = "()[]{}"
s = "]"
#s = "(]"
#s = "{[]}"
s = "([}}])"
sol = Solution()
sol.isValid(s)
print("s", s, "ans", sol.isValid(s))