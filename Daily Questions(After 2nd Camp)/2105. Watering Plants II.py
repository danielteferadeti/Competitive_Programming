class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l, r = 0, len(plants)-1
        fill_count = 0
        l_cap, r_cap = capacityA, capacityB
        
        while l <=r:
            if l==r:
                max_of_2 = max(l_cap, r_cap)
                if max_of_2 >= plants[l]: break
                else:
                    fill_count+=1
                    l_cap = capacityA - plants[l]
                    l +=1
            else:
                if plants[l] <= l_cap:
                    l_cap -= plants[l]
                    l +=1
                else:
                    fill_count+=1
                    l_cap = capacityA - plants[l]
                    l +=1
                if  plants[r] <= r_cap:
                    r_cap -= plants[r]
                    r -=1
                else:
                    fill_count+=1
                    r_cap = capacityB - plants[r]
                    r -=1
                    
        return fill_count