class Solution:
    def maximumSwap(self, num: int) -> int:
        temp = str(num)
        
        for i in range(len(temp)):
            foundBigger = False
            biggerIdx = i
            for j in range(i+1, len(temp)):
                if temp[j] > temp[i] and temp[j] >= temp[biggerIdx]:
                    foundBigger = True
                    biggerIdx = j
            if foundBigger:
                j = biggerIdx
                temp = temp[:i] + temp[j] + temp[i+1:j] + temp[i] + temp[j+1:]
                break
        
        return int(temp)