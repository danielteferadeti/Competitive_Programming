class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bothNum = 0
        
        for num in nums: bothNum ^= num
        
        lastBit_of_bothNum = bothNum & -bothNum
        
        num1, num2 = 0,0
        
        for num in nums:
            if num&lastBit_of_bothNum: num1 ^= num
            else: num2 ^= num
        
        return [num1, num2]