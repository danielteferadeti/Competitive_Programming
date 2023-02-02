class Solution:
    def numberOfWays(self, s: str) -> int:
        zeroPre = []
        onePre = []
        
        zeroCount = 0
        oneCount = 0
        
        for num in s:
            if int(num) == 0:
                zeroCount += 1
            else: oneCount += 1
            
            zeroPre.append(zeroCount)
            onePre.append(oneCount)
        
        total = 0
        for i in range(len(s)):
            if int(s[i]) == 0:
                leftOne = onePre[i]
                rightOne = onePre[-1] - onePre[i]
                
                total += (leftOne * rightOne)
            else:
                leftZero = zeroPre[i]
                rightZero = zeroPre[-1] - zeroPre[i]
                
                total += (leftZero * rightZero)
        
        return total
            