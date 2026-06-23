class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}

        for val in strs:
            list_value = list(sorted(val))
            sorted_value = ''.join(list_value)

            if sorted_value not in seen:
                seen[sorted_value]=[]
            
            
            seen[sorted_value].append(val)

        return list(seen.values())