class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        value = set()
        index=0

        for num in nums:
            if num not in value:
                nums[index]=num
                index+=1
                value.add(num)
        return index
        