class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        
        neg = dividend < 0 or divisor < 0 
        if dividend < 0 and divisor < 0: neg = 0

        dividend = abs(dividend) 
        divisor = abs(divisor)

        for i in range(31,-1,-1): # starting our loop

            if divisor << i <= dividend  :
                dividend-= divisor << i 
                quotient += 1 << i

        quotient = quotient if neg == 0 else -1 * quotient
        
        if quotient > 2**31 - 1: return 2**31 - 1
        
        elif quotient < -1 *(2**31): return -1 *(2**31)
        
        return quotient