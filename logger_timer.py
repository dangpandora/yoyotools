use decorator to create log and runtime file 

from functools import wraps 

def my_logger(ori_fun):
     import logging
     logging.basicConfig(filename= '{}.log'.format(ori_fun.__name__), level=logging.INFO)

     #wraps(ori_fun)
     def wrapper(*args, **kwargs):
         logging.info(
                 'Ran with args {}, and kwargs: {}'.format(args, kwargs))
         return ori_fun(*args,**kwargs)
    
     return wrapper 


when use it 
@my_logger
def ori_fun():


#record runtime 
def my_timer(ori_func):

   import time

     #wraps(ori_fun)
   def wrapper(*args, **kwargs):
        t1=time.time()
        result=ori_func(*args, **kwargs)
        t2=time.time()-t1
        print('{} ran in : {} secs'.format(ori_func.__name__, t2))
        return result

   return wrapper
