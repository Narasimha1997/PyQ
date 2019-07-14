from pyQ.abstracts import PyQInputTask, PyQOutputTask, PyQPipelineTask
from pyQ.pythreads import pythread
from pyQ.task_queue import PyQueue

"""
  Input phase can be both non-threaded or threaded
  This is because, if we are using this library for computer vision problems, 
  we might use OpenCV for other libraries, which are not thread-safe
  so, if using thread safe methods, toggle threading = False in PyQPipeline object
"""

@pythread
def pipeline_phase_thread(pipeline_object):
    #for each phase in the pipeline, create a thread and allow it to execute
    print(pipeline_object.name + " started")
    pipeline_object.input()
    pass

@pythread
def pipeline_input_thread(pipeline_object) :

    print(pipeline_object.name + " started")
    pipeline_object.task()


def pipeline_input_nonthread(pipeline_object) :

    print(pipeline_object.name + "started in non-threaded mode")
    pipeline_object.task()



#the main pipeline class for running pipeline jobs
class PyQPipeline :

    def __init__(self, task_array, queue_dict, globals_ = {}, threaded_input = True) :

        self.task_array = task_array
        self.queue_dict = queue_dict
        self.globals_ = globals_
        self.threaded_input = threaded_input

    def execute(self) :
        
        self.execute_with_nonthreaded_input() if not self.threaded_input else self.execute_with_threaded_input()


    def create_queues(self) :
        queues = {}
        for queue in self.queue_dict :
            queues[queue['name']] = PyQueue(name = queue['name'], max_size = queue['size'])
            
        print('Created Queues : ', queues)

        return queues 
    

    def execute_with_threaded_input(self) :
        queues = self.create_queues()
        for task in self.task_array :

            if task['type'] == 'phase' and issubclass(task['object'].__class__, PyQPipelineTask):
                #prepare input queues 
                qs_ip = queues[task['input']]
                qs_op = []
                for q_name in task['outputs'] :
                    qs_op.append(queues[q_name])
                
                
                #prepare the object:
                task['object'].set_input_queue(qs_ip)
                task['object'].set_output_queues(qs_op)
                #start the object : 
                pipeline_phase_thread(task['object'])
            
            elif task['type'] == 'input' and issubclass(task['object'].__class__, PyQInputTask) :
                qs_op = []
                for q_name in task['outputs'] :
                    qs_op.append(queues[q_name])
                
                task['object'].set_output_queues(qs_op)

                pipeline_input_thread(task['object'])
            
            else :
                qs_ip = queues[task['input']]
                task['object'].set_input_queue(qs_ip)

                pipeline_phase_thread(task['object'])
            
        pass
    

    def execute_with_nonthreaded_input(self) :

        input_task = None
        for task in self.task_array :
            if task['type'] == 'phase' and issubclass(task['object'].__class__, PyQPipelineTask):
                #prepare input queues 
                qs_ip = queues[task['input']]
                qs_op = []
                for q_name in task['outputs'] :
                    qs_op.append(queues[q_name])
                
                
                #prepare the object:
                task['object'].set_input_queue(qs_ip)
                task['object'].set_output_queues(qs_op)
                #start the object : 
                pipeline_phase_thread(task['object'])
            
            elif task['type'] == 'input' and issubclass(task['object'].__class__, PyQInputTask) :
                
                input_task = task
            
            else :
                qs_ip = queues[task['input']]
                task['object'].set_input_queue(qs_ip)

                pipeline_phase_thread(task['object'])
        
        qs_op = []
        for q_name in input_task['outputs'] :
            qs_op.append(queues[q_name])
                
        input_task['object'].set_output_queues(qs_op)

        pipeline_input_thread(input_task['object'])
            

        
