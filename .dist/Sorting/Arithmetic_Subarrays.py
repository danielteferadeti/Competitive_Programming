class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        sub_arrs = []
        answer = []  
        for m in range(len(l)):
            sub_arrs.append(nums[l[m]:r[m]+1])
        
        for sub_arr in sub_arrs:
            sub_arr.sort()
        
        print(sub_arrs)
        for sub_arr in sub_arrs:
            if len(sub_arr) ==2:
                answer.append(True)
            else:
                
                is_arithmetic = True
                dif = sub_arr[1] - sub_arr[0]
                for i in range(len(sub_arr)-1):
                    if sub_arr[i+1] - sub_arr[i] != dif:
                        is_arithmetic = False
                        answer.append(False)
                        break
                if is_arithmetic:
                    answer.append(True) 
        return answer