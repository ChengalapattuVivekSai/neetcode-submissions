class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        #step 1 store inside the hash map dude
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        arr=[]

        # arr=list(freq.items())

        for num,count in freq.items():
            arr.append([count,num])
        arr.sort()
        print("here is the array===",arr)
        result=[]

        while len(result) < k:
            result.append(arr.pop()[1])
        return result
        