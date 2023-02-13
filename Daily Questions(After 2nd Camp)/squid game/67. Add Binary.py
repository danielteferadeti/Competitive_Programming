class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def addbinary(first, second):
            result = ""
            carry = "0"
            for i in range(len(first)-1,-1,-1):
                if first[i] == "1" and second[i] == "1":
                    if carry == "0":
                        result += "0"
                        carry = "1"
                    else:
                        result += "1"
                        carry = "1"
                elif first[i] == "0" and second[i] == "0":
                    if carry == "0":
                        result += "0"
                        carry = "0"
                    else:
                        result += "1"
                        carry = "0"
                elif first[i] == "1" or second[i] == "1":
                    if carry == "0":
                        result += "1"
                        carry = "0"
                    else:
                        result += "0"
                        carry = "1"
            
            if carry == "1":
                result += "1"
            
            return "".join(result[::-1])
        
        if len(a) > len(b):
            dif = len(a) - len(b)
            b = "0"*dif + b
        elif len(b) > len(a):
            dif = len(b) - len(a)
            a = "0"*dif + a
        
        return addbinary(a,b)
                