class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            found = target - nums[i]

            if found in seen:
                return [seen[found],i]

            seen[nums[i]]=i
