class Solution:
    def checkValidString(self, s: str) -> bool:
        starCount = []
        stack = []
        for idx, char in enumerate(s):
            if char == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    if len(starCount) > 0:
                        starCount.pop()
                        continue
                    else:
                        return False
            else:
                if char == "(":
                    stack.append((char, idx))
                else:
                    starCount.append(idx)
        
        if stack:
            while stack and starCount and stack[-1][1] <= starCount[-1]:
                stack.pop()
                starCount.pop()
        
        return True if (not stack) else False