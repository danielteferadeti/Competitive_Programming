class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(coord):
            return coord[0] >= 0 and coord[1] >= 0 and coord[0] < len(board) and coord[1] < len(board[0])
        
        changeToLive = []
        changeToDead = []
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        
        visited = set()
        
        queue = deque()
        queue.append((0,0))
        visited.add((0,0))
        
        while queue:
            cur = queue.popleft()
            
            aliveOnes = 0
            
            for dirc in directions:
                nr, nc = cur[0]+dirc[0], cur[1]+dirc[1]
                
                if isValid((nr,nc)):
                    aliveOnes += board[nr][nc]==1
                    
                    if (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            
            if board[cur[0]][cur[1]] == 1:
                if aliveOnes < 2:
                    changeToDead.append(cur)
                elif aliveOnes == 2 or aliveOnes == 3:
                    continue
                else:
                    changeToDead.append(cur)

            else:
                if aliveOnes==3: changeToLive.append(cur)
        
        for r,c in changeToLive:
            board[r][c] = 1
        for r,c in changeToDead:
            board[r][c] = 0
        
        return board
            