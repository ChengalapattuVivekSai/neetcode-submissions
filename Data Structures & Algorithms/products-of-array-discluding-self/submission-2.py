class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        for i in range(len(nums)):

            mul=1

            for k in range(len(nums)):

                if k==i:
                    continue
                
                mul*=nums[k]
            
            result.append(mul)
        
        return result
        