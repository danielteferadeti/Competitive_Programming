class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = defaultdict(set)
        
        for user, time in logs:
            users[user].add(time)
        
        UAM = defaultdict(int)
        
        for user in users:
            UAM[len(users[user])] += 1
        
        res = []
        for i in range(1, k+1):
            res.append(UAM[i])
        
        return res