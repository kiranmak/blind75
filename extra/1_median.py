'''
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
import sys
from typing import List

#intuition:
    
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1   #swap 2 arrays
        
        total = len(nums1) + len(nums2)
        half = total //2
        
        infi = sys.maxsize
        
        l, r = 0, len(nums1) -1
        while True:
            i = (r + l) //2
            j = half - i - 2  # -2 is for indexing
            
            left1 = nums1[i] if i >= 0 else -infi
            right1 = nums1[i + 1] if (i + 1) < len(nums1) else infi
            left2 = nums2[j] if j >= 0 else -infi   
            right2 = nums2[j + 1] if (j +1) < len(nums2) else infi
            
            if left1 <= right2 and left2 <= right1:
                if total % 2: # odd
                    return min(right1, right2)  # return median from right partition
                # even
                return (max(left1, left2) + min(right1, right2))/2
            else:
                if left1 > right2:
                   r = i - 1  
                else:
                    l = l + 1
                    
s = Solution()
#print(s.findMedianSortedArrays([1,2], [3,4])) # --> 2.5
print(s.findMedianSortedArrays([], [1])) # --> 1