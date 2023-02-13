# class Node:
#     def __init__(self, val=1):
#         self.val = val
#         self.next = None
#         self.prev = None

# class LinkedList:
#     def __init__(self):
#         self.headval = None
class AllOne:
    def __init__(self):
        self.keyToValue = defaultdict(int)        
        self.maxHeap = []
        self.minHeap = []
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)
        
    def inc(self, key: str) -> None:
        self.keyToValue[key] += 1
        heapq.heappush(self.maxHeap, (-self.keyToValue[key], key))
        heapq.heappush(self.minHeap, (self.keyToValue[key], key))

        
    def dec(self, key: str) -> None:
        self.keyToValue[key] -= 1
        if self.keyToValue[key] == 0:
            del self.keyToValue[key]
        else:
            heapq.heappush(self.maxHeap, (-self.keyToValue[key], key))
            heapq.heappush(self.minHeap, (self.keyToValue[key], key))
        

    def getMaxKey(self) -> str:
        while self.maxHeap:
            if self.maxHeap[0][1] not in self.keyToValue or self.maxHeap[0][0] != -1*self.keyToValue[self.maxHeap[0][1]]:
                heapq.heappop(self.maxHeap)
                continue
            break
            
        return self.maxHeap[0][1] if self.maxHeap else ""
    
    def getMinKey(self) -> str:
        while self.minHeap:
            if self.minHeap[0][1] not in self.keyToValue or self.minHeap[0][0] != self.keyToValue[self.minHeap[0][1]]:
                heapq.heappop(self.minHeap)
                continue
            break
                
        return self.minHeap[0][1] if self.minHeap else ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()