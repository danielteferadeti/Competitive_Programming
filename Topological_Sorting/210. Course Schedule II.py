class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}
        visited = set()
        beingVisited = set()
        result = []
        
        for course, prerq in prerequisites:
            adjList[course].append(prerq)
            
        def dfs(crs: int) -> bool:
            
            if crs in beingVisited:
                return False
            if crs in visited:
                return True
            
            beingVisited.add(crs)
            for prer in adjList[crs]:
                k = dfs(prer)
                if k==False:
                    return False
            
            beingVisited.remove(crs)
            visited.add(crs)
            result.append(crs)
            return True
        
        for i in range(numCourses):
            h = dfs(i)
            if h== False:
                return []
        return result