class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        given = str(num)
        
        _dict = {}
        _dict[0] = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        _dict[1] = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        _dict[2] = ["","","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        _bet = {}
        _bet[1] = "Thousand"
        _bet[2] = "Million"
        _bet[3] = "Billion"
        
        resultStack = []
        
        num_itr = len(given)//3
        _betCount = 0
        if num_itr >= 1:
            l, r = len(given)-3, len(given)-1
            for i in range(num_itr):
                ind = 0
                while ind <= 2:
                    cur = int(given[r])
                    if ind==0:
                        if int(given[r-1]) ==1: resultStack.append(_dict[1][cur])
                        else: resultStack.append(_dict[0][cur])
                    elif ind == 1:
                        if cur != 1: resultStack.append(_dict[2][cur])
                    elif ind == 2:
                        if _betCount ==0 and cur!=0: 
                            resultStack.append("Hundred")
                            resultStack.append(_dict[0][cur])
                        else:
                            if cur!=0: resultStack.append("Hundred")
                            resultStack.append(_dict[0][cur])
                    ind+=1
                    r-=1
                
                _betCount +=1
                if _betCount < 3:
                    if l-1>=0 and int(given[l-1]) !=0 : resultStack.append(_bet[_betCount])
                    elif l -2>=0 and int(given[l-2]) !=0 : resultStack.append(_bet[_betCount])
                    elif l -3>=0 and int(given[l-3]) !=0 : resultStack.append(_bet[_betCount])
                l -= 3
        
        if len(given)%3 != 0:
            l, r = 0, len(given)%3 -1
            if _betCount ==0:
                if l==r: resultStack.append(_dict[0][int(given[r])])
                elif int(given[l]) ==1: resultStack.append(_dict[1][int(given[r])])
                else: 
                    resultStack.append(_dict[0][int(given[r])])
                    resultStack.append(_dict[2][int(given[l])])
            elif _betCount==1:
                if l==r: resultStack.append(_dict[0][int(given[r])])
                elif int(given[l]) == 1: resultStack.append(_dict[1][int(given[r])])
                else: 
                    resultStack.append(_dict[0][int(given[r])])
                    resultStack.append(_dict[2][int(given[l])])
                    
            elif _betCount == 2:
                if l==r: resultStack.append(_dict[0][int(given[r])])
                elif int(given[l]) == 1: resultStack.append(_dict[1][int(given[r])])
                else:
                    resultStack.append(_dict[0][int(given[r])])
                    resultStack.append(_dict[2][int(given[l])])
            else:
                resultStack.append(_bet[_betCount])
                resultStack.append(_dict[0][int(given[r])])
        
        result = ""
        for i in range(len(resultStack)-1, -1, -1):
            if resultStack[i]!="": result += resultStack[i] + " "
        return result[:len(result)-1]