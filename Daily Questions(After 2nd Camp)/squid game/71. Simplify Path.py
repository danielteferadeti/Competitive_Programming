class Solution:
    def simplifyPath(self, path: str) -> str:
        given = path.split("/")
        stack = []
        stack.append("/")
        
        for i in range(len(given)):
            cur = given[i]
            top = stack.pop(-1)
            if cur == "":
                if i + 1 == len(given):
                    pass
                else:
                    stack.append(top)
            else:
                if i + 1 == len(given):
                    if cur == ".":
                        pass
                    elif cur == "..":
                        if len(stack) !=0:
                            stack.pop(-1)
                            stack.pop(-1)
                        else:
                            stack.append(top)
                    else:
                        stack.append(top)
                        stack.append(cur)
                else:
                    if cur == ".":
                        stack.append(top)
                    elif cur == "..":
                        if len(stack) !=0:
                            stack.pop(-1)
                        else:
                            stack.append(top)
                    else:
                        stack.append(top)
                        stack.append(cur)
                        stack.append("/")
        if len(stack) == 0:
            return "/"
        
        result = ""
        while stack:
            result += stack.pop(0)
        
        return result
                