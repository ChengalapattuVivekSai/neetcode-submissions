class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch=='{' or ch=='[':
                stack.append(ch)
            
            elif (ch=='}' or ch ==']' or ch==')') and stack:

                if ((stack[-1]=='(' and ch==')') or (stack[-1]=='{' and ch=='}') or
                 (stack[-1]=="[" and ch==']')):
                    stack.pop()
                else:
                    return False
            else:
                return False
            
          
        if not stack:
            return True
        else:
            return False
        