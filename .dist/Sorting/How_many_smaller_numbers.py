class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            cnt_num = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    cnt_num +=1
            result.append(cnt_num)
        return result