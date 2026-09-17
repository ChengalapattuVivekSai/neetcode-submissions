class Solution:
    def isValid(self, s: str) -> bool:
        #so here we need to three ways where as 
        # loop trough the array if open bracket put inside the stack

        # if closed bracket then check the recent top elemtn of the stack  compare and its presnet elemtn mataches then for sure we need pop the stack element and move fowared 
        #repeat these step until reaching ending if still stack hsa element congrualte you are false 
        #if stack is empty bro you won and its trueee
        stack= []

        #base condition 

        for ch in s:
            if ch=='{' or ch=='[' or ch=='(':
                stack.append(ch)
            
            if ch=='}' or ch==']' or ch==')':
                if not stack:
                    return False

                value = stack[-1]

                if value=='[' and ch==']' or value=='{' and ch=='}' or value=='(' and ch==')':
                    stack.pop()
                else:
                    return False
                  
            
        
        if not stack:
            return True
        return False