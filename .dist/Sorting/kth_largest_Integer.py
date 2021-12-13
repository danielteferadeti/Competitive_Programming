class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        converted = []
        
        for elmt in nums:
            heapq.heappush(converted, int(elmt)*-1)
            
        for i in range(k-1):
            heapq.heappop(converted)
        
        return str(heapq.heappop(converted)*-1)