import pyQ 
import time, random

class Input(pyQ.PyQInputTask) :

    def __init__(self, name, globals_={}):
        pyQ.PyQInputTask.__init__(self, name, globals_=globals_)
    
    def task(self):
        while True :
            number = random.randint(a = 10, b = 100)
            self.output(number)


class EvenNumber(pyQ.PyQPipelineTask) :

    def __init__(self, name, globals_={}):
        pyQ.PyQPipelineTask.__init__(self, name, globals_=globals_)
        self.globals_ = globals_

    def task(self, value) :
        if value in self.globals_["values"] : 

            return value
        return 0

class FileWriter(pyQ.PyQOutputTask) :

    def __init__(self, name, globals_={}):
        pyQ.PyQOutputTask.__init__(self, name, globals_=globals_)
    
    def task(self, value) :
        
        if value != 0 :

            open('demo.txt', 'a').write(str(value) + "\n")


#create global variable 
globals_ = {
    "values" : [i for i in range(40, 80)]
}


queues = [
    {"name" : "Queue1", "size" : 100},
    {"name" : "Queue2", "size" : 200},
    {"name" : "Queue3", "size" : 300}
]

tasks = [
    {
        "type" : "input",
        "outputs" : ["Queue1"],
        "object" : Input(name = 'Input1')
    },
    {
        "type" : "phase",
        "outputs" : ["Queue2"],
        "input" : "Queue1",
        "object" : EvenNumber(name = 'EvenNumber', globals_ = globals_)
    },
    {
        "type" : "output",
        "input" : "Queue2",
        "object" : FileWriter(name = 'Output1')
    }
]



pyQ.PyQPipeline(task_array = tasks, queue_dict = queues, globals_ = globals_).execute()