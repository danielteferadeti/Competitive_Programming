class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        countDict = defaultdict(int)
        
        for num in nums:
            countDict[num] += 1
            
        ans = 0
        for i in range(len(target)):
            first = target[:i]
            second = target[i:]
            
            if first in countDict and second in countDict:
                if first == second:
                    n = countDict[first]
                    ans += 2*((n * (n-1))//2)
                else:
                    ans += countDict[first] * countDict[second]
        
        return ans