class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1,0)])
        visited = set()
        visited.add((0,1,0))
        
        while queue:
            curPos, speed, stepCount = queue.popleft()
            
            if curPos == target:
                return stepCount
            
            #Acc
            nextPos = curPos + speed
            acc = (nextPos, speed*2, stepCount+1)
            
            if (nextPos, speed*2) not in visited:
                queue.append(acc)
                visited.add((nextPos, speed*2))
            
            #Reverse
            reverse = (curPos, 1, stepCount+1) if speed < 0 else (curPos, -1, stepCount+1)
            if (reverse[0], reverse[1]) not in visited:
                queue.append(reverse)
                visited.add((reverse[0], reverse[1]))
                