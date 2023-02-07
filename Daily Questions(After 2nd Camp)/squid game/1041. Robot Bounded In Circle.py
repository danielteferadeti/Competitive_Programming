class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        newInst = instructions * 4
        
        curPos = (0,0)
        facing = 0 # 0 1 2 3
        
        travel = 0
        for i in range(len(newInst)):
            curInst = newInst[i]
            
            if curPos == (0,0):
                if travel//len(instructions) != 0 and travel%len(instructions)==0:
                    return True
            
            if curInst == "G":
                if facing == 0:
                    curPos = (curPos[0], curPos[1]+1)
                elif facing == 1:
                    curPos = (curPos[0]-1, curPos[1])
                elif facing == 2:
                    curPos = (curPos[0], curPos[1]-1)
                elif facing == 3:
                    curPos = (curPos[0]+1, curPos[1])
            elif curInst == "R":
                facing = (facing + 3) % 4
            else:
                facing = (facing + 1) % 4
            
            travel += 1
            
        if curPos == (0,0):
            if travel//len(instructions) != 0 and travel%len(instructions)==0:
                return True
            
        return False