class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #step1 we are here to solve this
        # freq = {}
        # for index,num in enumerate(nums):
        #     complement = target-num
        #     if complement in freq:
        #         return [freq[complement],index]
        #     freq[num]=index
        # return []
        left = 0
        # right = len(nums)-1
        # while left<right:
        #     total = nums[left]+nums[right]
        #     if total == target:
        #         return [left,right]
        #     elif total > target:
        #         right-=1
        #     else:
        #         left+=1
        # return []

        # freq = {}

        # for index,num in enumerate(nums):
        #     complement = target - num

        #     if complement in freq:
        #         return [freq[complement],index]
        #     freq[num] = index
        # return []

        freq = {}
        
        for index,num in enumerate(nums):
            complement = target - num
            if complement in freq:
                return [freq[complement],index]
            freq[num]=index
        return []






























        













