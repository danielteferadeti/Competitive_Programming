#Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if len(s) < 2:
            return False 
        
        for char in s:
            if char == '(' or char=='{' or char=='[':
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                from_stack = stack.pop()
                if from_stack == '(' and char != ')':
                    return False
                elif from_stack == '[' and char != ']':
                    return False 
                elif from_stack =='{' and char != '}':
                    return False
                
        if len(stack)>0:
            return False 
        
        return True