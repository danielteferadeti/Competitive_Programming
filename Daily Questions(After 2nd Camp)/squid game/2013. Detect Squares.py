class DetectSquares:
    def __init__(self):
        self.colByX = defaultdict(set)
        self.pointCount = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.colByX[x].add((x,y))
        self.pointCount[(x,y)] += 1
        
    def count(self, point: List[int]) -> int:
        multiplyBy = 1
        point1 = (point[0], point[1])
        
        verticalPoints = self.colByX[point1[0]]
        sqCount = 0
        for point2 in verticalPoints:
            if point2 == point1:
                continue
                
            distance = abs(point1[1] - point2[1])
            
            point_3_left = (point2[0]-distance, point2[1])
            point_3_right = (point2[0]+distance, point2[1])
            
            point_4_left = (point1[0]-distance, point1[1])
            point_4_right = (point1[0]+distance, point1[1])
            
            if point_3_left in self.pointCount and point_4_left in self.pointCount:
                multiplyBy = (self.pointCount[point2] * self.pointCount[point_3_left] * self.pointCount[point_4_left])
                sqCount += multiplyBy
                multiplyBy = 1
                
            if point_3_right in self.pointCount and point_4_right in self.pointCount:
                multiplyBy = (self.pointCount[point2] * self.pointCount[point_3_right] * self.pointCount[point_4_right])
                sqCount += multiplyBy
                multiplyBy = 1
                
        return sqCount
                
                
            

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)