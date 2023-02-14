class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = collections.Counter(str(n))
        
        for pwr in range(31):
            if count == collections.Counter(str(1 << pwr)):
                return True
            
        return False