from pprint import PrettyPrinter, pprint
from body_parser import body_parser
import pickle

class Request:
        
        def __init__(self, method: str, uri: str, protocol: str, headers: dict, body: dict):
            self.method = method
            self.uri = uri
            self.protocol = protocol
            self.headers = headers
            self.body = body
        
        
        def __str__(self):
            pp = PrettyPrinter(indent=4)
            return f"""method: {self.method}
    uri: {self.uri}
    protocol: {self.protocol}

    headers: {pp.pformat(self.headers)}

    body: {pp.pformat(self.body)}"""



class request_parser:
    body_parser = body_parser()
    
    def __init__(self):
        pass
    
    def parse(self, request: str) -> dict:
        """
        Note: this parsing of the request can go wrong in many ways. it is not fully compliant with the HTTP specifications, 
        but should work for most of the cases.
        if you are comfortable with the HTTP protocol, please do not hesitate to improve this function to meet the specs, thanks!    
        """
        # this is the object that will be returned after parsing the request and filling it
        request_as_object = {
                            "method": None,
                            "uri": None,
                            "protocol": None,
                            "headers": None,
                            "body": None
                            }
        # getting the different parts of the HTTP request: request line, headers, and the body
        request_parts = request.split("\r\n")

        request_line = request_parts[0]
        headers = request_parts[1:-2]
        body = request_parts[-1]
        
        # parsing the first line of the request, that contains the method, the uri (ressource requested) and the protocol
        request_line_parts = request_line.split(" ")
        request_as_object["method"] = request_line_parts[0]
        request_as_object["uri"] = request_line_parts[1]
        request_as_object["protocol"] = request_line_parts[2]
        
        # parsing the headers part to get a dictionary of headers
        headers_obj = {}
        for header in headers:
            header_parts = header.split(": ")
            headers_obj[header_parts[0]] = header_parts[1]
        request_as_object["headers"] = headers_obj
        
        # parsing the cookies in the headers
        if "Cookie" in headers_obj:
            cookies = self.parse_cookies(headers_obj["Cookie"])
            request_as_object["cookies"] = cookies
        
        # parsing the body with the body parser only if the method is not GET
        if request_as_object["method"] != "GET":
            body = self.body_parser.parse(body, headers_obj["Content-Type"])
            request_as_object["body"] = body
        else :
            body = {}
        
        
        
        
    def parse_cookies(self, cookies):
        cookies_obj = {}
        cookies = [cookie.split("=") for cookie in cookies.split(";")]
        for cookie in cookies:
            key = cookie[0]
            value = cookie[1]
            cookies_obj.update({key: value})
            
        return cookies_obj
    
        
reqp = request_parser()
with open("get_req.ser", "rb") as f:
    req = pickle.load(f)
    reqp.parse(req.decode())