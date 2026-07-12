class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setValue = set()

        for val in nums:
            if val in setValue:
                return True
            else:
                setValue.add(val)
                
        return False
            
        