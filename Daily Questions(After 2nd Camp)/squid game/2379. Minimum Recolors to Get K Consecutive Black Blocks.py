class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whiteCount = []
        total = 0
        for color in blocks:
            if color == "W": total += 1
            
            whiteCount.append(total)
        
        l,r = 0,k-1
        bestMin = 10**10
        
        while r < len(blocks):
            dif = (whiteCount[r] - whiteCount[l]) + 1 if blocks[l] == "W" else (whiteCount[r] - whiteCount[l])
            bestMin = min(bestMin, dif)
            
            l+=1
            r+=1
        
        return bestMin