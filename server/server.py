from socket import *
from threading import Thread
from HTTP.request_parser import request_parser # class that will parse the incoming HTTP requests
from HTTP.response_builder import response_builder # class that will build the response that we want to send

class Server:
    def add_error(self, status, handler):
        self.error_handlers[status] = handler
    def handle_error(self, status, req, res):
        (self.error_handlers.get(status) or self.error_handler)(status, req, res)
    def error_handler(self, status, req, res): # ONLY FOR ERRORS CALLED USING HANDLE_ERROR!
        res.send({
            404 : "<h1>This Resource Was Not Found On This Server<h1>",
            405 : "<h1>This Method Is Not Allowed On This Resource</h1>"
        }[status], status=status)
        
    def __init__(self, host="127.0.0.1", port=8000):
        self.host = host
        self.port = port
        # the server is a socket that is bound to the the given host and port at the call of the start function
        # and starts listening for incoming requests
        self.server = socket(AF_INET, SOCK_STREAM)
    
        self.request_parser = request_parser()
        
        # this is the dictionnary that will map the routes to their handlers (callback functions)
        self.map_path_handler = {
            "GET": {},
            "POST": {},
            "PUT": {},
            "DELETE": {},
            "HEAD": {},
            "OPTIONS": {},
            "TRACE": {},
            "CONNECT": {}
        }
        self.error_handlers = {}
        
        
    # these are the function that map each route to it's supported method, and the callback function
    # that handles it, in the self.map_path_handler dictionnary
    def get(self, path, handler):
        self.map_path_handler["GET"].update({path: handler})
    
    def post(self, path, handler):
        self.map_path_handler["POST"].update({path: handler})
    
    def put(self, path, handler):
        self.map_path_handler["PUT"].update({path: handler})
    
    def delete(self, path, handler):
        self.map_path_handler["DELETE"].update({path: handler})
        
    def head(self, path, handler):
        self.map_path_handler["HEAD"].update({path: handler})
        
    def options(self, path, handler):
        self.map_path_handler["OPTIONS"].update({path: handler})
        
    def trace(self, path, handler):
        self.map_path_handler["TRACE"].update({path: handler})
        
    def connect(self, path, handler):
        self.map_path_handler["CONNECT"].update({path: handler})
        
    
    def request_handler(self, conn: socket):
        # receiving the request from client and parse it with the request_parser class
        request = self.request_parser.parse(conn.recv(1024).decode()) ## I think this might fail for longer HTTP requests but I'll assume this works
        response = response_builder(conn)

        # Note: here i should check for the "Connection" header in the request
        # if it's set to "close" should close the socket connection after sending the response
        # if it's set to "keep-alive" i should keep the socket connectin alive
        # but for some reason it makes the web page on the browser bug
        # so i will just close the connection every time for now
        
        
        # here i check if a handler exists for the requested route and execute it with the res (response_builder) and req (the parser request) parameters
        # if it does not exist i send back "404 Not found" error message, or "405 method not allowed"
        if request.method in self.map_path_handler.keys():
            if request.uri in self.map_path_handler[request.method].keys():
                self.map_path_handler[request.method][request.uri](request, response)
            else:
                # i think instianciating the response_builder class for every response is not super efficient too
                # i should find a better way to build responses with this class
                self.handle_error(404, request, response)
        else:
            self.handle_error(405, request, response)
            
    
        conn.close()
            
        
        
        
        
    def start(self, debug=False):
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        if debug:
            print(f"Server is running on http://{self.host}:{self.port}")
        # server starts listening to incomming connections
        while True:
            conn, addr = self.server.accept()
            # each connection is handled in a seperate thread with the request-handler function (is this efficient ? probably not)
            request_thread = Thread(target=self.request_handler, args=(conn,))
            request_thread.start()
            
        

        
    
        
        
