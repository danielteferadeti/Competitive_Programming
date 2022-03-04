class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        solution = []
        
        for x in range(1, 1001):
            for y in range(1, 1001):
                if customfunction.f(x,y) == z:
                    solution.append((x,y))
                elif customfunction.f(x,y) > z: 
                    break
        return solution