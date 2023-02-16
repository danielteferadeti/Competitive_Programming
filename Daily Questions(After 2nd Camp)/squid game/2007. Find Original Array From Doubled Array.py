class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count_dict ={}
        changed.sort()
        
        result = []
        
        print(changed)
        for elmt in changed:
            if elmt in count_dict:
                count_dict[elmt] +=1
            else:
                count_dict[elmt] = 1

        for key in changed:
            if key*2 in count_dict:
                cur_val = count_dict[key]
                found_val = count_dict[key*2]
                
                if cur_val > 0 and cur_val <= found_val:
                    count_dict[key] -= 1
                    count_dict[key*2] = count_dict[key*2] - 1
                    result.append(key)
        
        for key in count_dict:
            if count_dict[key] !=0:
                return []
            
        return result