class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left=0
        right=len(numbers)-1

        while left<right:
            sum_target = numbers[left] + numbers[right]

            if sum_target<target:
                left+=1
            
            if sum_target>target:
                right-=1
            
            if sum_target==target:
                return [left+1,right+1]

        return []
        