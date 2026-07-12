class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #first thing store in hashmap and compare it values if greate than1

        freq={}

        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        for value,key in freq.items():
            if key>1:
                return True
        
        return False




        