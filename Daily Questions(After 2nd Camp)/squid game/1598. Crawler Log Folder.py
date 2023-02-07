class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for opr in logs:
            if opr != "./" and opr != "../":
                stack.append(opr)
            else:
                if opr == "../":
                    if stack: stack.pop()
        return len(stack)