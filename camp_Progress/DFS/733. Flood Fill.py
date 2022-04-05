class Solution:
    def solver(self, curCoor:(int, int), newColor: int, givenColor: int, givenImage: List[List[int]],colLen: int, rowLen: int):
        i,j = curCoor
        if givenImage[i][j] == givenColor:
            givenImage[i][j] = newColor
        
        #Move Up
        if i - 1 >= 0 and givenImage[i-1][j] == givenColor:
            curCoor = (i -1, j)
            self.solver(curCoor,newColor,givenColor,givenImage,colLen,rowLen)
        #Move down
        if i + 1 < rowLen and givenImage[i +1][j] == givenColor:
            curCoor = (i+1, j)
            self.solver(curCoor,newColor,givenColor,givenImage,colLen,rowLen)
        #Move Left
        if j - 1 >= 0 and givenImage[i][j - 1] == givenColor:
            curCoor = (i, j -1)
            self.solver(curCoor,newColor,givenColor,givenImage,colLen,rowLen)
        #move Right 
        if j + 1 < colLen and givenImage[i][j +1] == givenColor:
            curCoor = (i, j+1)
            self.solver(curCoor,newColor,givenColor,givenImage,colLen,rowLen)
        return givenImage


    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rowLen = len(image)
        colLen = len(image[0])
        
        curCoor = (sr,sc)
        givenColor = image[sr][sc]
        
        if givenColor == newColor:
            return image
        
        return self.solver(curCoor,newColor,givenColor,image,colLen,rowLen)