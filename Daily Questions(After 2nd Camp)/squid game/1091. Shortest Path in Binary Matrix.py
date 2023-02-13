class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0: return -1
        def isValid(dirc):
            r, c = dirc
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid)
    
        queue = deque([])
        visited = set()
        level = 1
        
        queue.append((0,0))
        visited.add((0,0))
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        
        while queue:
            curLevel = len(queue)
            
            while curLevel > 0:
                r, c = queue.popleft()
                
                if (r, c) == (len(grid)-1, len(grid)-1): 
                    return level
                
                for dirc in directions:
                    nr, nc = r+dirc[0], c + dirc[1]
                    if isValid((nr,nc)) and (nr,nc) not in visited and grid[nr][nc]== 0:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        
                curLevel -= 1
            
            level += 1
        
        return -1
            
        