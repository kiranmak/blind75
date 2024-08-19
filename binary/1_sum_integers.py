'''
371. Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3
Example 2:
Input: a = 2, b = 3
Output: 5
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        print(f"a={a}, carry=0, b={b}")
        while b !=0:
            carry = a & b # both a and b have changed
            a = a ^ b
            b = carry << 1
            print(f"a={a}, carry={carry}, b={b}")
        return a

s = Solution()

print(s.getSum(10,3)) # -> 8                        