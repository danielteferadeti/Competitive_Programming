class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        busToStation = {}
        stationToBus = defaultdict(list)
        
        for idx, busRoutes in enumerate(routes):
            busToStation[idx] = set(busRoutes)
            
            for station in busRoutes:
                stationToBus[station].append(idx)
        
        queue = deque([])
        
        sourceBus = stationToBus[source]
        visited = set()
        
        for bus in sourceBus:
            visited.add(bus)
            queue.append((bus, 1))
        
        while queue:
            curBus, count = queue.popleft()
            
            for station in busToStation[curBus]:
                if station == target:
                    return count
                for bus in stationToBus[station]:
                    if bus not in visited:
                        visited.add(bus)
                        queue.append((bus, count+1))
        
        return -1
        