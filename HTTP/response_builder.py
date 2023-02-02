from socket import socket
from HTTP.http_statuses import statuses


"""
this response builder is still not fully compliant to the HTTP specifications but it gets the job done for now
i will improve it later
"""

class response_builder:    
    
    BASIC_HTTP_TEMPLATE = "HTTP/1.1 {status} {status_string}\r\n"
    
    def __init__(self, conn: socket):
        self.conn = conn
    
    def send(self, data: any, status: int=200, headers: dict={}) -> None:
        res = response_builder.BASIC_HTTP_TEMPLATE
        res = res.format(status=status, status_string=statuses[status])
        headers_str = ""
        if len(headers.keys())>0:
            headers_str: str = self.build_headers(headers)
        res += headers_str + "\r\n"
        res += data
        
        print(res)
        self.conn.sendall(res.encode())
    
    def render(self, html_file_path: str, status: int=200, headers: dict={}) -> None:
        pass
    def sendFile(self, file_path: str, status: int=200, header: dict={}) -> None:
        with open(file_path, "rb") as f:
            self.conn.sendfile(f)
        
            
            
            
    def build_headers(self, headers):
        headers_str = ""
        for header in headers.keys():
            headers_str += f"{header}: {headers[header]}\r\n"       
            
        return headers_str
            
            
            
            
            
            
            
            
            
            
            
            
            