class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def compressed(word):
            counter = []
            count = 0
            prev = word[0]
            compressed = ""
            for char in word:
                if char == prev: 
                    count += 1
                else:
                    compressed += prev
                    counter.append(count)
                    count = 1
                    prev = char
                    
            compressed += prev
            counter.append(count)
            return (compressed, counter)
        
        s, count = compressed(s)
        ans = 0
        for word in words:
            compWord, wordCount = compressed(word)
            if compWord == s:
                isValid = True
                for i in range(len(count)):
                    if (count[i] != wordCount[i] and count[i] < 3) or count[i] < wordCount[i]:
                        isValid = False
                        break
                if isValid:
                    ans += 1
        
        return ans