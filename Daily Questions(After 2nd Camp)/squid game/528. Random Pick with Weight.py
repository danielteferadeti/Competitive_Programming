class Solution:
    def __init__(self, w: List[int]):
        self.preSum = []
        total = 0
        
        for num in w:
            total += num
            self.preSum.append(total)
         
    def pickIndex(self) -> int:
        randSum = random.randint(1, self.preSum[-1])
        
        return bisect.bisect_left(self.preSum, randSum)
        
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()