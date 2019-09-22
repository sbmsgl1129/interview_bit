class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentCount = 0
        self.hashMap  = {}
        self.queue    = []
        
    # @return an integer
    def get(self, key):
        
        if key in self.hashMap:
            value = self.hashMap[key]
            
            self.queue.remove(key)
            self.queue.append(key)
            
            return value
        else:
            return -1
    
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hasMap:
            
            self.hashMap[key] = value
            
            self.queue.remove(key)
            self.queue.append(key)
            
        elif self.currentCount == self.capacity:
            
            keyToRemove  = self.queue.pop(0)
            del self.hashMap[keyToRemove]
            
            self.queue.append(key)
            self.hashMap[key] = value
        else:
            self.queue.append(key)
            self.hashMap[key] = value
            
            self.currentCount += 1
        
        return
