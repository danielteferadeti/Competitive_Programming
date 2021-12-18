class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if str(char) != ")":
                stack.append(str(char))
            else:
                k = stack.pop()
                temp = ""
                while k!= "(":
                    temp += k
                    k= stack.pop()
        
                stack.append(temp[::-1])
        if len(stack) !=1:
            temp = ""
            while len(stack)>0:
                temp += stack.pop()
            stack.append(temp)
            
        return stack.pop()[::-1]
        