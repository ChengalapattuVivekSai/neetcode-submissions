from math import ceil
from typing import List

class Solution:
    #helpeer function antaru broooo
    def countTime(self,piles: List[int],hours:int)->int:
        total_hours =0
        for i in range(0,len(piles)):
            total_hours+=ceil(piles[i]/hours)
        return total_hours

    # main functions broooo 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #step 1 start doing binary search from left to max list

        left = 1
        right = max(piles)
        # ans = right

        while left<=right:
            mid = (left + right)//2

            totalHours = self.countTime(piles,mid)

            if totalHours <=h:
                ans = mid
                right=mid-1 
            else:
                left = mid + 1

        return ans
        



        
        