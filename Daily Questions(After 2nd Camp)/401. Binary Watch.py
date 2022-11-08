class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        '''
        #bit-Manipulation Iteratively
        
        def countBits(num):
            count = 0
            while num>0:
                lastBit = num & 1
                if lastBit: count+=1
                num = num >> 1
            return count
        
        ans = []
        for hr in range(0,12):
            for mnt in range(0,60):
                if (countBits(hr) + countBits(mnt))==turnedOn:
                    hour,minute = str(hr), "0" + str(mnt)
                    
                    res = hour + ":" + minute[-2:]
                    ans.append(res)
        
        return ans
        '''
        
        #BackTracking 
        
        time_representation = "0000000000"
        def solver(turnedOn, time_representation, startAt):
            if turnedOn==0:
                hours = int(time_representation[:4],2)
                minutes = int(time_representation[4:],2)
                
                if hours < 12 and minutes < 60: #save the valid hour and minute combinations only!
                    minutes = "0" + str(minutes)
                    res = str(hours) + ":" + minutes[-2:]
                    answer.append(res)
                return answer
            
            else:
                for i in range(startAt, 10):
                    if time_representation[i]=="0":
                        #change one bit and explore --- then backtrack
                        time_representation = time_representation[:i] + "1" + time_representation[i+1:]
                        solver(turnedOn-1, time_representation,i)
                        time_representation = time_representation[:i] + "0" + time_representation[i+1:]
            
            return answer
        
        answer = []
        if turnedOn > 8: return answer
        
        return solver(turnedOn, time_representation, 0)
        