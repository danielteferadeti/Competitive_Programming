# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        integ = {'0' ,'1','2', '3','4','5','6', '7', '8', '9'}
        i = 0
        while i < len(s):
            if s[i] == '[':
                stack.append(s[i])
                
            elif s[i] in integ or s[i] == "-":
                num = s[i]
                while i < len(s) - 1 and s[i+1] in integ:
                    i += 1
                    num += s[i]
                    
                stack.append(int(num))
                
            elif s[i] == ']':
                nested = []
                while stack[-1] != '[':
                    nested.append(stack.pop())
                
                nested = nested[::-1]
                stack.pop()
                stack.append(nested)
                
            i += 1
        
        ans = stack.pop()
        
        def nestedResult(cur):
            if type(cur) == int:
                return NestedInteger(cur)

            nestedList = NestedInteger()

            for val in cur:
                chagedVal = nestedResult(val)
                nestedList.add(chagedVal)
                
            return nestedList
        
        return nestedResult(ans)
        
        