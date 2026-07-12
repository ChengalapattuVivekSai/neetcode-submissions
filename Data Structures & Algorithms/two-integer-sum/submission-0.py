class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for index,num in enumerate(nums):
            complement=target - num
            if complement in freq:
                return [freq[complement],index]
            freq[num]=index
        return []
                