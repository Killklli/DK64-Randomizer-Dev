'Decorator function for UI elements to bind events to buttons.'
from functools import wraps
from pyodide import create_proxy
from js import document
def bind(event,id,iterations=0):
	'Bind a function to an event for a buttton.\n\n    Args:\n        event (str): Event to bind to eg: click\n        id (str): ID of the element to bind to.\n        iterations (int, optional): If we want to run this function multiple times with an increasing iteration. Defaults to 0.\n    ';C=iterations;B=event
	def A(function):
		'Return the main decorator back this is the main response.\n\n        Args:\n            function (func): The original function.\n\n        Returns:\n            func: The original function to return.\n        ';A=function;A=create_proxy(A)
		if C==0:document.getElementById(id).addEventListener(B,A,False)
		else:
			for D in range(0,C):
				try:document.getElementById(id+str(D)).addEventListener(B,A)
				except Exception:pass
		@wraps(A)
		def E(*B,**C):'Wrap our existing function with our passed function.\n\n            Returns:\n                func: The function to wrap.\n            ';D=A(*(B),**C);return D
		return E
	return A