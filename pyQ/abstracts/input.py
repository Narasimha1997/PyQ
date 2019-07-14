from pyQ.pythreads import pythread
import time

class PyQInputTask :

    def __init__(self, name, globals_ = {}) :

        self.name = name
        self.globals = globals_
        self.output_queues = None
        self.items_processed = 0
    

    def set_output_queues(self, queue) :

        self.output_queues = queue
    

    #extend this method to output elements to the queue
    def output(self, value) :
        for output_queue in self.output_queues :
            while output_queue.isFull() : 
                time.sleep(0.1)
            #write to the queue
            output_queue.insert(value)
        self.items_processed +=1
        #acknowledge, can be ignored
        return True
    
    def get_items_processed(self):

        return self.items_processed
    
    #this is the abstract task method, write your input task here
    def task(self) :
        pass
    





    
