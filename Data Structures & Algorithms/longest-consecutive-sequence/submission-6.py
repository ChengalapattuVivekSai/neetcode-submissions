class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #its time compelixy is o(n**2)

        #step 1 choosing a element and find out in the array and the appending is huge

        # sort elements + add into set  then if every elmement is having +1 then its consisectuvie 
        if not nums:
            return 0

      
        final_array = list(set(nums))

        final_array.sort()

        current = 1
        longest =1
       
        clear_array = list(final_array)

        for i in range(len(clear_array)-1):
            if clear_array[i]+1==clear_array[i+1]:
                current+=1
            else:
                current = 1

            longest = max(longest, current)
        
        return longest
        
        

        