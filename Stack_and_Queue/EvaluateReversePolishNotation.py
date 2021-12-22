class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        heap = ["+", "-","*","/"]
        heapq.heapify(heap)
        
        for var in tokens:
            if var in heap:
                if len(stack)!=0:
                    second_num = int(stack.pop())
                    first_num = int(stack.pop())
                    num = 0
                    if var=="/":
                        num = int(first_num/second_num)
                    elif var=="*":
                        num = int(first_num*second_num)
                    elif var=="+":
                        num = int(first_num+second_num)
                    elif var=="-":
                        num = int(first_num-second_num)
                    stack.append(num)
            else:
                stack.append(var)
                
        return stack.pop()