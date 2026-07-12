class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq={}
        list_value=[]

        for i in range(0,len(strs)):
            sorted_char="".join(sorted(strs[i]))

            freq[sorted_char]=freq.get(sorted_char,[]) + [strs[i]]

        return list(freq.values())
        