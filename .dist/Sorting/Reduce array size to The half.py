class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        elmt_count = {}
        result_que = []
        heapq.heapify(result_que)
        
        for elmt in arr:
            if elmt in elmt_count:
                elmt_count[elmt] +=1
            else:
                elmt_count[elmt] = 1
                
        nums = elmt_count.keys()
        if len(nums) == len(arr):
            return int(len(arr)/2)
     
        k = int(len(arr)/2)
        while k >0:
            choosen = -1
            min_dif = sys.maxsize
            for key in elmt_count:
                if key in result_que:
                    pass
                else:
                    check = k - elmt_count[key]
                    if min_dif > check:
                        min_dif = check
                        choosen = key
            if choosen >0:
                heapq.heappush(result_que, choosen)
                k -= elmt_count[choosen]
            
        return len(result_que)