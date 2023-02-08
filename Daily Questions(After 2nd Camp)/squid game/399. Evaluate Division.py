class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        
        for pair in equations:
            first, second = pair
            if first not in adjList: adjList[first].append((first, 1))
            if second not in adjList: adjList[second].append((second, 1))
            
        for idx, pair in enumerate(equations):
            first, second = pair
            adjList[first].append((second, values[idx]))
            adjList[second].append((first, 1/values[idx]))
        
        
        def dfs(lookfor, cur, multiple):
            if lookfor == cur:
                res[0] = multiple
                return
            
            for nib, mult in adjList[cur]:
                if nib not in visited:
                    visited.add(nib)
                    dfs(lookfor, nib, multiple*mult)
        ans = []
        for query in queries:
            first, second = query
            
            if first not in adjList or second not in adjList:
                ans.append(-1)
                continue
            
            firstList = adjList[first]
            found = False
            for nib1, mult1 in firstList:
                visited = set([second])
                res = [0]
                dfs(nib1, second, 1)
                
                if res[0]:
                    ans.append(mult1/res[0])
                    found = True
                    break
            if not found:
                ans.append(-1)
  
        return ans