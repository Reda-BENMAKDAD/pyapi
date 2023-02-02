from socket import *
from threading import Thread
from HTTP.request_parser import request_parser


class Server:
    
    def __init__(self, host="127.0.0.1", port=8000):
        self.host = host
        self.port = port
        self.server = socket(AF_INET, SOCK_STREAM)
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
        request = conn.recv(1024).decode()
        request_p = request_parser()
        request = request_p.parse(request)
        
        keep_alive: bool = True
        if "Connection" in request.headers:
            if request.headers["Connection"] == "close":
                keep_alive = False
                
        if request.method in self.map_path_handler.keys():
            if request.uri in self.map_path_handler[request.method].keys():
                handler = self.map_path_handler[request.method][request.uri]
                handler(request, conn)
            else:
                conn.send("HTTP/1.1 200 ok\r\n\r\n sorry, ressource not found on this server".encode())
        else:
            conn.send("HTTP/1.1 200 ok\r\n\r\n sorry, ressource not found on this server".encode())
             
        
        conn.close()
            
        
        
        
        
    def start(self, debug=False):
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        if debug:
            print(f"Server is running on http://{self.host}:{self.port}")
        while True:
            conn, addr = self.server.accept()
            request_thread = Thread(target=self.request_handler, args=(conn,))
            request_thread.start()
            
        

        
    
        
        