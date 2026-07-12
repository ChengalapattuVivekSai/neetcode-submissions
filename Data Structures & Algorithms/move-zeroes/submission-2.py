class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        writer = 0


        for val in nums:
            if val!=0:
                nums[writer] = val
                writer+=1
            
        for i in range(writer,len(nums)):
            nums[i]=0

        
