class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        slice_list = []
        count_dict = {}
        result = []
        
        start = 0
        end = 10
        
        if len(s) < 10:
            return []
        
        while start < len(s):
            slice_list.append(s[start:end])
            start +=1
            end +=1
            
        for elmnt in slice_list:
            if elmnt not in count_dict:
                count_dict[elmnt] = 1
            else:
                count_dict[elmnt] +=1
        for elmnt in count_dict:
            if count_dict[elmnt] > 1:
                result.append(elmnt)
                
        return result
        
        