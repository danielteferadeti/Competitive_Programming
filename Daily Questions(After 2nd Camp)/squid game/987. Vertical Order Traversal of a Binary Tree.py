# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = defaultdict(list)
        
        queue = deque([ (root, 0, 0) ])
        
        while queue:
            node, col, level = queue.popleft()
            
            if not node:
                continue
                
            results[(col,level)].append(node.val)
            results[(col,level)].sort()
            
            queue.append((node.left, col-1, level+1))
            queue.append((node.right, col+1, level+1))
            
        
        sortedkeys = list(results.keys())
        sortedkeys.sort()
        
        Finalresult = defaultdict(list)
        for col, level in sortedkeys:
            Finalresult[col] += results[(col, level)]

        return Finalresult.values()