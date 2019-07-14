from pyQ.pythreads import pythread
import time

class PyQPipelineTask :

    def __init__(self, name, globals_ = {}) :

        self.name = name
        self.globals_ = globals_
        self.input_queue = None
        self.output_queues = None
        self.items_processed = 0
        self.items_fetched = 0
    
    def set_input_queue(self, queue) :
        self.input_queue = queue
    
    def set_output_queues(self, queue) :
        self.output_queues = queue

    def output(self, value) :
        for output_queue in self.output_queues :
            while output_queue.isFull() :
                time.sleep(0.1)
            output_queue.insert(value)
        self.items_processed +=1
        return True
    
    def input(self) :

        while True :
            if not self.input_queue.isEmpty() :
                self.items_fetched +=1
                value = self.input_queue.delete()
                #print(value)
                output_value = self.task(value)
                self.output(output_value)
    

    def get_items_processed(self) :

        return self.items_processed
    
    def get_items_fetched(self) :

        return self.items_fetched
    
    #this is the task , the task should return the value to be written to the queue
    def task(self, value) :

        pass
