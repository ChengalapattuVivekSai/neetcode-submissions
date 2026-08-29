class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left =0
        check_val = set()
        max_len =0
        

        for right in range(len(s)):
            while s[right] in check_val:
                check_val.remove(s[left])
                left+=1
                
            check_val.add(s[right])
            max_len = max(max_len,len(check_val))
            
        
        return max_len


        