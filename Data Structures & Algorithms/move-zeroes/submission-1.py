class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #step one we need to keep a left =0 and right=i+1
        write=0
        for num in nums:
            if num!=0:
                nums[write]=num
                write+=1
        
        for i in range(write,len(nums)):
            nums[write]=0
            write+=1

        

         

            


