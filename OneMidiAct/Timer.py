import time


class Timer:
   
    def __init__(self):
         self.start_time=time.time_ns()//1000000
         self.counter=0
       
    def get_time(self):
        current_time=time.time_ns()//1000000
        real_time=current_time-self.start_time
        if real_time>self.counter:
            self.counter=real_time
        return self.counter
        
        
    def stop(self):
        stop_time=time.time_ns()
        self.start_time=stop_time

