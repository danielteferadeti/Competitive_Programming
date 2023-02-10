class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:        
        bestMax = 0
        img1Ones = []
        img2Ones = []
        shiftCount = defaultdict(int)

        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1: img1Ones.append((i, j))
                if img2[i][j] == 1: img2Ones.append((i, j))

        for r_1, c_1 in img1Ones:
            for r_2, c_2 in img2Ones:
                rowShift, ColShift = r_1 - r_2, c_1 - c_2
                shiftCount[(rowShift, ColShift)] += 1
                
                bestMax = max(bestMax, shiftCount[(rowShift, ColShift)])

        return bestMax