from pyQ.pythreads import pythread
import time


class PyQOutputTask:

    def __init__(self, name, globals_ = {}) :

        self.name = name
        self.globals_ = globals_
        self.items_fetched = 0
        self.items_processed = 0
        self.input_queue = None
    

    def set_input_queue(self, queue) :

        self.input_queue = queue
    

    def task(self, value) :
        #override this method to perform action
        pass
    
    def input(self) :

        while True :

            if not self.input_queue.isEmpty() :
                
                value = self.input_queue.delete()
                self.items_fetched +=1
                output_value = self.task(value)
                self.output(value)
                self.items_processed +=1

    
    def output(self, value) :
        #the abstract output method , override this to output values to external world
        pass
    

