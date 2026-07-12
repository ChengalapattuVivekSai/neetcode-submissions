from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped_freq = defaultdict(list) #it store grouped values

        orderd= ''

        for word in strs:

            list_word = sorted(word)

            ordered = ''.join(list_word)

            grouped_freq[ordered].append(word)
            
        
        return list(grouped_freq.values())