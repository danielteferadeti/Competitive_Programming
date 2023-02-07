class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lineDict = {}
        pharaLine = []
        
        i = 0
        while i < len(words):
            curLine = ""
            spaces = 0
            while len(curLine) <= maxWidth and i < len(words):
                temp = curLine + " " + words[i] if curLine != "" else words[i]
                if len(temp) <= maxWidth:
                    if curLine != "": spaces += 1
                    curLine = temp
                    i += 1
                else:
                    break
            
            pharaLine.append(curLine)
            lineDict[len(pharaLine)-1] = spaces
            
        ans = []
        for idx, line in enumerate(pharaLine):
            spaceLeft = maxWidth - len(line)
            if spaceLeft > 0 and idx != len(pharaLine)-1:
                lineSpaces = lineDict[idx]
                if lineSpaces == 0:
                    line = line + " "*spaceLeft
                    ans.append(line)
                    continue
                    
                evenToAll = spaceLeft//lineSpaces
                
                forLeftPart = spaceLeft - (lineSpaces * evenToAll)
                i = 0
                temp = line
                added = 0
                for j in range(len(line)):
                    if line[j] == " " and i < forLeftPart:
                        temp = temp[:j+added] + " " + " "*evenToAll + temp[j+added:]
                        i += 1
                        added += 1 + evenToAll
                    elif line[j] == " ":
                        temp = temp[:j+added] + " "*evenToAll + temp[j+added:]
                        added += evenToAll
                ans.append(temp)
                
            elif spaceLeft > 0 and idx == len(pharaLine)-1:
                line = line + " "*spaceLeft
                ans.append(line)
            else:
                ans.append(line)
        
        return ans
                
                