class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        freq = {}

        for i,val in enumerate(nums):
            complement = target - val

            if complement in freq:
                return [freq[complement],i]
            
            freq[val] = i
        return []

        