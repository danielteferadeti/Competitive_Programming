class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        nextStart = []
        for i in range(len(sequence)):
            if sequence[i]==word[0]:
                nextStart.append(i)
        
        Bestcount = 0
        for start in nextStart:
            seqCount = 0
            i = start
            while i < len(sequence):
                if sequence[i:i+len(word)] == word:
                    seqCount += 1
                    i = i+len(word)
                else:
                    break
            
            Bestcount = max(Bestcount, seqCount)
        return Bestcount
                    
                