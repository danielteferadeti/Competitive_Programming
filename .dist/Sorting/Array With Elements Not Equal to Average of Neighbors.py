class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        j = len(nums) -1
        result = []
        
        while i<=j:
            if i ==j:
                result.append(nums[i])
                break
            result.append(nums[i])
            result.append(nums[j])
            j-=1
            i+=1
            
        return result
        