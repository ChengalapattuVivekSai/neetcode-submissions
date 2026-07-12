class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        value ={}

        #this is one solution 
        # setValue = set()

        # for val in nums:
        #     if val in setValue:
        #         return True
        #     else:
        #         setValue.add(val)
                
        # return False

        #other way is my fav one
        for val in nums:
            value[val]=value.get(val,0) + 1

            if value[val]>1:
                return True

        return False
            

            
        