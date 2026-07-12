class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #so here we are having two ways to solve one is by hashmap and other is two pointer method
        
        #first we need to sort the array for proper arrangemnet
        nums.sort()
        res=[]
        total_sum=0
        #1 ist thing is we need to run a loop
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            while left<right:
                total_sum=nums[i] + nums[left] + nums[right]
                
                if total_sum==0:
                    res.append([nums[i],nums[left],nums[right]])

                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                        
                    left+=1
                    right-=1
                
                elif total_sum<0:
                    left+=1
                else:
                    right-=1
            
        return res
                    


        