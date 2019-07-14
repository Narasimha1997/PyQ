# PyQ
A python library for expressing computations using Message passing queues. 

### Backgroud 
We all know the concept of pipelines. A pipeline is a series of tasks or operations performed in the same order. For example
cars can be manufactured using Pipeline, where every stage adds a new component to the car body. Pipelines increase productivty 
because, at every stage in a pipeline, we can load a new input. You can takeup any course or watch videos regarding pipelines to understand better.
  Similarly , if we are developing an application that has large number of steps, one of the traditional way is to write them sequentially,it can be easier
  but not a good practice because the next input has to wait for current input to be processed completely. If we divide the large task 
  into modules / sub-tasks and make each task independant of each other,then every sub-task takes input performs some operation and sends it to the next task,
  as soon as it produces the output it can take up the next input, or it can simply wait. Productivity is increased here because of two reasons : 
  1. No need to wait for entire operation to get over
  2. Maintainence becomes easier as operation is divided into sub-tasks.
  
 ### Mathematical Modelling : 
 Suppose we have N inputs and K tasks are to be performed and t is some arbitrary time required to perfom some task,
 the total time would be  N * K , N inputs executed K times, suppose we build K times in pipeline, the time would be :
 K + N - 1, Factor K is present because first input takes K steps to execute, all other inputs take only N - 1 steps as they need not
 wait for previous input to complete. 
 
 ### Why this library ?
 Python is used for builing ML systems or some computations that require large number of steps. For example, in Video Intelligence, the typical 
 sequence will be to take input from video source, convert them to sequnece of frames , from frames to numpy arrays, feed it to a ML model , obtain inference,
 draw bounding boxes - using inference data, send the processed frame to any external system. If this operation is non-pileplined, efficiency reduces.
 If it is using pipeline, Each of these steps are processed independantly! 
 
 ### How it works ?
 This library allows you to write computation steps as independant tasks, each task is written as a class, every task takes input, process it and
 provides an output, These tasks are actually executed as threads inside a loop and is called whenever there is an input available. These tasks are connected internally using 
 a Queue, Queue can be of any size and connects two or more tasks. Every task takes input from queue, process it and place the output on another queue.
 
 
