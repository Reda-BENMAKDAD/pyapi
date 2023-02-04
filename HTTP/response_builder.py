from socket import socket
from HTTP.http_statuses import statuses
import json

"""
this response builder is still not fully compliant to the HTTP specifications but it gets the job done for now
i will improve it later
"""

class Response:
    BASIC_HTTP_TEMPLATE = "HTTP/1.1 {status} {status_string}\r\n"
    
    def __init__(self, conn: socket):
        self.conn = conn
        self.status = 200
    
    def send(self, data: any, status: int=200, headers: dict={}) -> None:
        self.status = status
        # TODO: Get length of response for Content-Length 
        res = Response.BASIC_HTTP_TEMPLATE.format(status=status, status_string=statuses[status])
        res += self.build_headers(headers) + "\r\n"
        res += data
        self.conn.sendall(res.encode())
    
    def render(self, html_file_path: str, status: int=200, headers: dict={}) -> None:
        self.status = status
        pass
    def sendFile(self, file_path: str, status: int=200, header: dict={}) -> None:
        self.status = status
        with open(file_path, "rb") as f:
            self.conn.sendfile(f)
        
    def json(self, json_data: dict, status: int=200, headers: dict={}) -> None:
        self.send(json.dumps(json_data))
            
            
    def build_headers(self, headers):
        headers_str = ""
        for header in headers:
            headers_str += f"{header}: {headers[header]}\r\n"       
            
        return headers_str
            
            
            
            
            
            
            
            
            
            
            
            
            
