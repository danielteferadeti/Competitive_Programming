class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_dict = {}
        words.sort()        
        for elmt in words:
            if elmt in count_dict:
                count_dict[elmt] +=1
            else:
                count_dict[elmt] = 1
        
        return heapq.nlargest(k,count_dict.keys(), key = count_dict.get)