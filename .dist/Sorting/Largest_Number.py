class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_dict = {}
        result = ""
        only_zero = True
        
        for elmt in nums:
            if elmt != 0:
                only_zero = False
            temp = str(elmt)*10          
            if temp in num_dict:
                num_dict[temp].append(elmt)
            else:
                num_dict[temp] = [elmt]
                
        order = []
        for key in num_dict:
            order.append(key)
        
        order.sort()
        order = order[::-1]
        
        for elmt in order:
            original = num_dict[elmt]
            for num in original:
                result += str(num)
    
        if only_zero:
            return "0"
        return result