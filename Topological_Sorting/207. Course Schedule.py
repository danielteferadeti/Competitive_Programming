class Solution:
    def dfs(self,i: int,adjList: dict(), visited: set()) -> bool:
        if i not in visited:
            visited.add(i)
        else:
            return False
        
        if len(adjList[i]) == 0:
            visited.remove(i)
            return True
        
        for prerq in adjList[i]:
            k = self.dfs(prerq,adjList,visited)
            if k:
                adjList[i].remove(prerq)
            else:
                return False
            
        visited.remove(i)
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        visited = set()
        
        for course, prerq in prerequisites:
            adjList[course].append(prerq)
        
        #print(adjList)
        
        result = True
        for i in range(numCourses):
            if len(adjList[i]) !=0:
                result = self.dfs(i,adjList,visited)
            if not result:
                return result
        return result