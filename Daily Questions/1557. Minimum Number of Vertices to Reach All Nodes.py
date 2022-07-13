class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        include= set()
        not_include = set()

        for edge in edges:
            begin = edge[0]
            end = edge[1]
            not_include.add(end)
            include.add(begin)

        for i in not_include:
            if i in include:
                include.remove(i)

        return include