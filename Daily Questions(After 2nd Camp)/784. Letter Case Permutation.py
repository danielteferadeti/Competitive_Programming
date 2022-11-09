class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = set()
        
        def solver(idx, strr):
            ans.add(strr)
            
            if idx >= len(strr):
                return
            
            if strr[idx].isnumeric():
                solver(idx+1, strr)
            else:
                solver(idx+1, strr)
                if strr[idx].isupper():
                    strr = strr[:idx] + strr[idx].lower() + strr[idx+1:]
                    solver(idx+1, strr)
                else:
                    strr = strr[:idx] + strr[idx].upper() + strr[idx+1:]
                    solver(idx+1, strr)
            
            return
        
        solver(0,s)
        
        return list(ans)