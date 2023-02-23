class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:  
        rec1_x_start, rec1_y_start = rec1[0],rec1[1]
        rec1_x_end, rec1_y_end = rec1[2],rec1[3]
        
        rec2_x_start, rec2_y_start = rec2[0],rec2[1]
        rec2_x_end, rec2_y_end = rec2[2],rec2[3]
        

        if rec1_x_start >= rec2_x_end or rec2_x_start >= rec1_x_end or rec1_y_start >= rec2_y_end or rec2_y_start >= rec1_y_end:
            return False

        return True
        
        