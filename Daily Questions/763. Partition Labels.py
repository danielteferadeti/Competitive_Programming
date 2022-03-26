class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ind_char = {}
        result = []
        max_partition = 0
        max_right_end = 0
        
        for i, char in enumerate(s):
            last_ind_char[char] = i
            
        for i, char in enumerate(s):
            max_partition +=1
            max_right_end = max(max_right_end, last_ind_char[char])
            
            if i == max_right_end:
                result.append(max_partition)
                max_partition = 0
                
        return result 