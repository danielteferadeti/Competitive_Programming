class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = deque([])
        visited = set()
        result = set()
        
        queue.append(("(",n-1,n))
        
        while queue:
            par, openPar, closePar = queue.popleft()
            r = len(par)-1
            given,close = par,closePar
            if given[r]=="(":
                while r >=0 and given[r]=="(" and close > 0:
                    given = given + ")"
                    close -= 1

                    if openPar==0 and close==0:
                        result.add(given)
                    else:
                        forNext = (given, openPar, close)
                        if forNext not in visited:
                            visited.add(forNext)
                            queue.append(forNext)
                    r-=1
            else:
                if openPar == 0:
                    given += ")"*closePar
                    result.add(given)
                else:
                    while openPar < close:
                        given = given + ")"
                        close -= 1
                        if (given, openPar, close) not in visited:
                            visited.add((given, openPar, close))
                            queue.append((given, openPar, close))
            
            given = par
            while openPar > 0:
                given = given + "("
                openPar -= 1
                
                if (given, openPar, closePar) not in visited:
                    visited.add((given, openPar, closePar))
                    queue.append((given, openPar, closePar))
        
        final = list(result)
        final.sort()
        return final
