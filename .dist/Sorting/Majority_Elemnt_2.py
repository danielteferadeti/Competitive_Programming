class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elmt_dict = {}
        result = []
        
        for elmt in nums:
            if elmt not in elmt_dict:
                elmt_dict[elmt] = 1
            else:
                elmt_dict[elmt] =  elmt_dict[elmt] +1
        
        for key in elmt_dict:
            if elmt_dict[key] > len(nums)/3:
                result.append(key)
        return result