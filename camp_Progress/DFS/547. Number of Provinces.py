class Solution:
    def is_connected_to(self, city: int, visited: set, isConnected: List[List[int]]):
        visited.add(city)
        for nighbor in range(len(isConnected[0])):
            if isConnected[city][nighbor] == 1 and nighbor not in visited:
                self.is_connected_to(nighbor, visited, isConnected)
        
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_connected = 0
        visited = set()
        
        for city in range(len(isConnected)):
            if city not in visited:
                num_connected += 1
                self.is_connected_to(city,visited, isConnected)
                
        return num_connected