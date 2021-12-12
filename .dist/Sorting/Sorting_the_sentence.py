class Solution:
    def sortSentence(self, s: str) -> str:
        w_list = s.split()
        order = []
        result = ""
        for k in range(len(w_list)):
            order.append("")
        
        for i in range(len(w_list)):
            w_num = int(w_list[i][len(w_list[i])-1])
            order[w_num-1] = w_list[i][0:len(w_list[i])-1]
        
        for j in range(len(order)):
            if j != len(order)-1:
                result += order[j] + " "
            else:
                result += order[j]
        
        return result