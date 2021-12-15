class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coins = 0
        i = len(piles) -2
        
        while i > int(len(piles)/3) -1:
            max_coins += piles[i]
            i -=2
            
        return max_coins
    
