class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total_neg = 0
        last_neg = -1

        for row in grid:
            r = len(row) -1
            l = 0

            while l <= r:
                m = (l + r) // 2
                if row[m] < 0:
                    r = m - 1
                    last_neg = m
                else:
                    l = m + 1
            if last_neg != -1:
                total_neg += len(row) - last_neg
        return total_neg