class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def cal_div(divisor):
            total = 0
            for num in nums:
                if num % divisor == 0:
                    total += num//divisor
                else:
                    total += (num//divisor) + 1
            return total
        max_n = max(nums)
        smallest_divisor = -1
        l = 1
        r = max_n
        while l <= r:
            m = (r + l)//2
            cur_sum = cal_div(m)

            if cur_sum <= threshold:
                smallest_divisor = m
                r = m -1
            else:
                l = m +1

        return smallest_divisor