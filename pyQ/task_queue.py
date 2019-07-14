import queue

class PyQueue :

    def __init__(self, name, max_size) :

        self.name = name
        self.queue = queue.Queue(max_size)
    

    def insert(self, value) :

        self.queue.put(value)
    
    def delete(self) :

        return self.queue.get()
    
    def isEmpty(self) :

        return self.queue.empty()
    
    def isFull(self) :

        return self.queue.full()
    
    def size(self) :

        return self.queue.qsize()
    