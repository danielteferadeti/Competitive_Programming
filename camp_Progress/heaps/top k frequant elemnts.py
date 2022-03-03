class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict = {}
        
        for elmt in nums:
            if elmt in count_dict:
                count_dict[elmt] +=1
            else:
                count_dict[elmt] = 1
        
        return heapq.nlargest(k,count_dict.keys(), key = count_dict.get)