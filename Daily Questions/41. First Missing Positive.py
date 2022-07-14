class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = max(nums)
        if max_num <=0:
            return 1
        num_set = set()
        
        for num in nums:
            num_set.add(num)
        
        for i in range(1, max_num):
            if i not in num_set:
                return i
        
        if max_num == 2**31 -1:
            return 2**31 -1
        
        return max_num + 1