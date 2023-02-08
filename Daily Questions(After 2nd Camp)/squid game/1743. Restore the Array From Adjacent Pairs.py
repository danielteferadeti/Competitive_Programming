class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        
        for x,y in adjacentPairs:
            adjList[x].append(y)
            adjList[y].append(x)
            
        queue = deque([])
        visited = set()
        ans = []
        
        for key in adjList:
            if len(adjList[key]) == 1:
                queue.append(key)
                visited.add(key)
                ans.append(key)
                break
        
        while queue:
            cur = queue.popleft()
            
            for nib in adjList[cur]:
                if nib not in visited:
                    visited.add(nib)
                    ans.append(nib)
                    queue.append(nib)
        
        return ans