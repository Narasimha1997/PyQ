from pyQ.pythreads import pythread
import time

class DemoClass :

    def __init__(self) :

        self.a = 10
    

    @pythread
    def thread_function(self) :

        while True :

            print (self.a + 1)
            time.sleep(1)