class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        
        for i in range(len(digits)-1,-1,-1):
            cur = digits[i]
            added = cur + 1 if i==len(digits)-1 else cur + carry
            
            if added >9: 
                carry = added//10
                added = added%10
            else:
                carry = 0
            
            digits[i] = added
        
        if carry!=0: digits.insert(0, carry)
        
        return digits