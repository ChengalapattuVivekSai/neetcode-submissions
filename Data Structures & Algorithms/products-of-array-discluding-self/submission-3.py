class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [1] *len(nums)
        left_result =[]
        left=1
        
        for val in nums:
            left_result.append(left)
            left=left*val

            
        right_result = [1]*len(nums)  #pre assinged size 

        right=1
        for i in reversed(range(len(nums))):
            right_result[i]=right
            right=right*nums[i]

        
        for i in range(0,len(nums)):
            final[i]=left_result[i]*right_result[i]
        
        return final
    

