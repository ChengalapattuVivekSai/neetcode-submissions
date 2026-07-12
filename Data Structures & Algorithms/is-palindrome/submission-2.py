class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_final = ""
        for ch in s:
            if ch.isalnum():
                s_final+=ch.lower()

        left = 0
        right = len(s_final)-1
        
        while left<=right:
            if s_final[left]!=s_final[right]:
                print("here what is the value failing",s_final[left],s_final[right])
                return False
            else:
                left+=1
                right-=1
        return True
            
        