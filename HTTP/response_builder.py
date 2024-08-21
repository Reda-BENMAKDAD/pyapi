from socket import socket
from HTTP.http_statuses import statuses
from os import stat
import json
from HTTP.mimeTypes import mimetypes

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
        res = Response.BASIC_HTTP_TEMPLATE.format(status=status, status_string=statuses[status])
        res += self.build_headers(headers) + "\r\n"
        res += data
        self.conn.sendall(res.encode())
    
    def render(self, html_file_path: str, status: int=200, headers: dict={}) -> None:
        self.status = status
        pass
    def sendFile(self, file_path: str, status: int=200, headers: dict={}) -> None:
        file_ext = "." + file_path.split(".")[-1]
        content_type = mimetypes.get(file_ext, "text/plain")
        bytes_file_size = stat(file_path).st_size
        
        headers["Content-Type"] = content_type
        headers["Content-Length"] = bytes_file_size + 100
        
        with open(file_path, "r") as f:
            file_content = f.read()
            
        response = self.BASIC_HTTP_TEMPLATE.format(status=status, status_string=statuses[status])
        response += self.build_headers(headers) + "\r\n"
        response += file_content
        print(response)
        self.conn.sendall(response.encode())

        
    def json(self, json_data: dict, status: int=200, headers: dict={}) -> None:
        response = self.BASIC_HTTP_TEMPLATE.format(status=status, status_string=statuses[status])
        headers["Content-Type"] = "application/json"
        response += self.build_headers(headers) + "\r\n"
        response += json.dumps(json_data)
        self.conn.sendall(response.encode())
            
            
    def build_headers(self, headers):
        headers_str = ""
        for header in headers:
            headers_str += f"{header}: {headers[header]}\r\n"       
            
        return headers_str
            
            
            
            
            
            
            
            
            
            
            
            
            
