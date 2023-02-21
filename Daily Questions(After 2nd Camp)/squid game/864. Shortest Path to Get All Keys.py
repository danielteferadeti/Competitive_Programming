class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        numberOfKeys = 0
        start = ()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].isalpha() and grid[i][j].islower():
                    numberOfKeys += 1                    
                if grid[i][j] == "@": start = (i,j)
        
        if not start: return -1
        
        def isValid(pair):
            r,c = pair
            return r >=0 and c >= 0 and r < len(grid) and c < len(grid[0])
        

        queue = deque([])
        dircs = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        steps = 0
        
        queue.append((*start, ""))
     
        while queue:
            level = len(queue)
            while level > 0:
                level -= 1
                i,j, keys = queue.popleft()
                # i,j = cur
                    
                if len(keys) == numberOfKeys:
                    return steps
                
                for r,c in dircs:
                    nr,nc = i+r, j+c
                    if isValid((nr,nc)) and grid[nr][nc] != "#" and (nr,nc, keys) not in visited:
                        visited.add((nr, nc,keys))
                        
                        if grid[nr][nc].isalpha() and grid[nr][nc].isupper() and grid[nr][nc].lower() not in keys:
                            continue
                        
                        if grid[nr][nc].isalpha() and grid[nr][nc].islower() and grid[nr][nc] not in keys:
                            temp = keys + grid[nr][nc]
                            queue.append((nr,nc, temp))
                        else:  
                            queue.append((nr,nc, keys))
                
            steps += 1
                
        return -1