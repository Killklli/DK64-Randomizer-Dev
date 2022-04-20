'Task file to run functions in the background via webworkers.'
import inspect,json,js
def background(function,args,returning_func):'Background a function via a webworker.\n\n    This is a fully isolated function, you can not access the UIs DOM.\n\n    Args:\n        function (func): The function we run after backgrounding.\n        args (list): List of args to pass to the function.\n        returning_func (func): Function to run once we complete the main function.\n    ';B=returning_func;A=function;D=inspect.getmodule(A);C=inspect.getsource(D);C+=str(A.__name__)+'('+','.join(args)+')';E=inspect.getmodule(B);js.background_worker.postMessage(json.dumps({'func':C,'returning_func':'from '+E.__name__+' import '+B.__name__}))