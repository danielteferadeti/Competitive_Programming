class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pnt_dist = {}
        result = []
        
        for j in range(len(points)):
            point = points[j]
            dist = point[0]*point[0] + point[1]*point[1]
            if dist not in pnt_dist:
                pnt_dist[dist] = [j]
            else:
                pnt_dist[dist].append(j)
        
        ordered = sorted(pnt_dist)
        a=0
        while a < k:
            for elm in pnt_dist[ordered[a]]:
                result.append(points[elm])
            a += len(pnt_dist[ordered[a]])

        return result