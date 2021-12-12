class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            cur_min = nums[i]
            min_ind = i
            for j in range(i+1, len(nums)):
                if cur_min > nums[j]:
                    cur_min = nums[j]
                    min_ind = j
            nums[i], nums[min_ind] = nums[min_ind], nums[i]

