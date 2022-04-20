'Run a self hosted HTTP server that has no cache tied to it.'
import http.server
PORT=8000
class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
	'No cache response handler.\n\n    Args:\n        http (http.server.SimpleHTTPRequestHandler): Properly tacks on the headers we need to expire the files.\n    '
	def send_response_only(A,code,message=None):'Tack on the headers and only send the response.\n\n        Args:\n            code (str): Code to send\n            message (str, optional): Message to respond with. Defaults to None.\n        ';super().send_response_only(code,message);A.send_header('Cache-Control','no-store, must-revalidate');A.send_header('Expires','0')
if __name__=='__main__':http.server.test(HandlerClass=NoCacheHTTPRequestHandler,port=PORT)