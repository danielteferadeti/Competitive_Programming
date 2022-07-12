class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = []
        
        for row in range(m):
            cur = []
            for clmn in range(n):
                cur.append("x")
            grid.append(cur)
        
        for G in guards:
            grid[G[0]][G[1]] = "g"
        
        for W in walls:
            grid[W[0]][W[1]] = "w"

        #to Right
        for i in range(m):
            j = 0
            while j < n:
                if grid[i][j]=="g":
                    j+=1
                    while j<n:
                        if grid[i][j] == "g" or grid[i][j] == "w":
                            break
                        grid[i][j] = "s"
                        j+=1
                else:
                    j+=1
        #To Left
        for i in range(m):
            j = n-1
            while j>=0:
                if grid[i][j]=="g":
                    j-=1
                    while j>=0:
                        if grid[i][j] == "g" or grid[i][j] == "w":
                            break
                        grid[i][j] = "s"
                        j-=1
                else:
                    j-=1
        #Downward 
        for j in range(n):
            i = 0
            while i<m:
                if grid[i][j]=="g":
                    i+=1
                    while i<m:
                        if grid[i][j] == "g" or grid[i][j] == "w":
                            break
                        grid[i][j] = "s"
                        i+=1
                else:
                    i+=1
        #upward
        for j in range(n):
            i = m-1
            while i>=0:
                if grid[i][j]=="g":
                    i-=1
                    while i>=0:
                        if grid[i][j] == "g" or grid[i][j] == "w":
                            break
                        grid[i][j] = "s"
                        i-=1
                else:
                    i-=1
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="x":
                    count+=1

        return count