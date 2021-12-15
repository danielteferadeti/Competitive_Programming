class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        max_opt = 0
        elmt_count = {}
        
        for elmt in nums:
            if elmt in elmt_count:
                elmt_count[elmt] +=1
            else:
                elmt_count[elmt] = 1
                
        # print(elmt_count)
        for num in nums:
            if num - k >=0:
                pass
            else:
                needed_val = k - num
                if needed_val in elmt_count:
                    if needed_val == num:
                        if elmt_count[needed_val] >1:
                            max_opt +=1
                            elmt_count[needed_val] -=2
                    else:
                        if elmt_count[needed_val] >=1 and elmt_count[num] >= 1:
                            max_opt +=1
                            elmt_count[needed_val] -=1
                            elmt_count[num] -=1
        # print(elmt_count)
        return max_opt