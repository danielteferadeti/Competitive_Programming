class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([])
        
        for i in range(len(tickets)):
            queue.append((tickets[i], i))
        
        timeCount = 0
        while queue:
            ticket, person = queue.popleft()
            timeCount += 1
            
            ticket -= 1
            
            if ticket == 0:
                if person == k: return timeCount
            else:
                queue.append((ticket, person))
        
        return timeCount