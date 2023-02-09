class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        sub_till_k = 0
        sub_til_k_1 = 0
        
        l,r = 0,0
        counter1 = defaultdict(int)
        while r < len(nums):
            counter1[nums[r]] += 1
            
            while len(counter1) > k:
                counter1[nums[l]] -= 1
                if not counter1[nums[l]]: del counter1[nums[l]]
                l += 1
            
            sub_till_k += (r - l) + 1
            r += 1
        
        l,r = 0,0
        counter2 = defaultdict(int)
        while r < len(nums):
            counter2[nums[r]] += 1
            
            while len(counter2) > k-1:
                counter2[nums[l]] -= 1
                if not counter2[nums[l]]: del counter2[nums[l]]
                l += 1
                
            sub_til_k_1 += (r - l) + 1
            r += 1
        
        return sub_till_k - sub_til_k_1
            