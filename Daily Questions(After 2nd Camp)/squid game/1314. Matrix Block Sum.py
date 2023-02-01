class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rowSum = [[0 for _ in range(len(mat[0]))] for i in range(len(mat))]
        ans = [[0 for _ in range(len(mat[0]))] for i in range(len(mat))]
        
        total = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if j-1 >=0:
                    rowSum[i][j] = rowSum[i][j-1] + mat[i][j]
                else: rowSum[i][j] = mat[i][j]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                up = min(i, k)
                down = min(len(mat)-1-i, k)
                right = min(len(mat[0])-1-j, k)
                left = min(j,k)
                
                rStart, rEnd = i - up, i + down
                cStart, cEnd = j - left, j + right
                
                total = 0
                for row in range(rStart, rEnd+1):
                    total += ((rowSum[row][cEnd] - rowSum[row][cStart]) + mat[row][cStart])
                
                ans[i][j] = total
                
        return ans
        