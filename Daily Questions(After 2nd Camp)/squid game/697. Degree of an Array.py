class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        for num in nums: count[num] += 1
        
        max_freq = max(count.values())
        sec_count = defaultdict(int)
        l,r = 0,0
        best_min = 10**10
        
        while r < len(nums):
            cur = nums[r]
            sec_count[cur] += 1
            if sec_count[cur] == max_freq:
                while l <= r and sec_count[cur] == max_freq:
                    best_min = min(best_min,(r - l)+1)
                    sec_count[nums[l]] -= 1
                    l += 1
                r += 1
            else:
                r += 1
        
        return best_min if best_min != 10**10 else max_freq