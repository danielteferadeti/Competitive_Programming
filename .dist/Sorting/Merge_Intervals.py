class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = [intervals[0]]
        
        for interval in intervals:
            int_str = interval[0]
            int_end = interval[1]
            
            int_not_found = True
            for i in range(len(result)):
                res_int_str = result[i][0]
                res_int_end = result[i][1]
                
                if int_str >= res_int_str and int_str <= res_int_end:
                    if int_end >=res_int_end:
                        result[i] = [res_int_str, int_end]
                    else:
                        result[i] = [res_int_str, res_int_end]
                    int_not_found = False
                elif res_int_str > int_str and res_int_str <= int_end:
                    if res_int_end >= int_end:
                        result[i] = [int_str, res_int_end]
                    else:
                        result[i] = [int_str, int_end]
                    int_not_found = False
            if int_not_found:
                result.append(interval)
        
        return result