class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []

        for val in nums:
            freq[val]=freq.get(val,0)+1

        #step2 from the dictionary we need to bring the values freq whis is greager then k pr equal to k
        # We need to sort the Dictionary and then get top k elements from the last(Better sort in descending and get )     
        
        #Conversion into tuple or Array using these
        freq_values=list(freq.items())

        sorted_items = sorted(freq_values,key =lambda x:x[1],reverse=True)

        for key,value in sorted_items:
            if k>0:
                result.append(key)
                k-=1

        return result