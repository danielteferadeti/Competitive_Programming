class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            two_stones = heapq.nlargest(2,stones)
            
            s1, s2 = two_stones[0], two_stones[1]
            
            if s1==s2:
                stones.remove(s1)
                stones.remove(s2)
            else:
                stones.remove(s1)
                stones.remove(s2)
                stones.append(s1 - s2)
        if stones:
            return stones[0]
        
        return 0