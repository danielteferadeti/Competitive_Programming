# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preOrder(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        values = data.split(",")
        
        def builder():
            if values[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(values[self.i]))
            self.i += 1
            
            node.left = builder()
            node.right = builder()
            
            return node
        
        return builder()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))