class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap  = capacity
        self.lruCache = {}
        self.left  = Node(-1,0)
        self.right = Node(-1,0)
        self.left.next   = self.right
        self.right.prev = self.left
        
    def get(self, key: int) -> int:
        if key in self.lruCache:
            self.delete(self.lruCache[key])
            self.add(self.lruCache[key])
            
            return self.lruCache[key].val
        
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.lruCache:
            self.delete(self.lruCache[key])
        
        self.lruCache[key] = Node(key,value)
        self.add(self.lruCache[key])
        
        if len(self.lruCache) > self.cap:
            LRU = self.left.next
            del self.lruCache[LRU.key]
            self.delete(LRU)  
    
    def add(self, node):
        prev = self.right.prev
        prev.next = node
        
        self.right.prev = node
        node.prev = prev
        node.next = self.right
            
    def delete(self, node):
        prev,nextNode = node.prev,node.next
        prev.next = nextNode
        nextNode.prev = prev
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)