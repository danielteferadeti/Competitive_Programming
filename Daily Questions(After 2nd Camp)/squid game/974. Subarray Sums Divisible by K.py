class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        summ = 0
        res = 0
        dic = {0:1}
        for a in nums:
            summ = (summ + a) % k
            if summ in dic:
                res += dic[summ]
                dic[summ] += 1
            else:
                dic[summ] = 1
        return res