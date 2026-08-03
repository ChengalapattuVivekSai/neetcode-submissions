class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        left = 0
        right=len(nums)-1
        
        i=0
        nums.sort()  #step1 sorting
        total=[]

        for i in range(0,len(nums)-2):
            
            if i>0  and nums[i]==nums[i-1]: #we can put while here because only if is possible
                continue
            left=i+1
            right=len(nums)-1
        
            while left < right:
                left_sum = nums[i] + nums[left]
                right_val =nums[right]

                if left_sum+right_val==0:
                    total.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left <right and nums[right]==nums[right+1]:
                        right-=1

                elif left_sum+right_val <0 :
                    left+=1

                else:
                    right-=1
            
        
        return total

        