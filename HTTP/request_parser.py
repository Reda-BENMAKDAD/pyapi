from pprint import PrettyPrinter
from HTTP.body_parser import BodyParser
from urllib.parse import unquote_plus
class Request:
        
    def __init__(self, method: str, uri: str, protocol: str, headers: dict[str, str], body: dict, cookies: dict, query : dict[str,str]):
        self.method = method
        self.uri = uri
        self.protocol = protocol
        self.headers = headers
        self.body = body
        self.query = query
        
        def __str__(self):
            pp = PrettyPrinter(indent=4)
            return f"""method: {self.method}
    uri: {self.uri}
    protocol: {self.protocol}
    headers: {pp.pformat(self.headers)}
    query: {pp.pformat(self.query)}
    body: {pp.pformat(self.body)}"""


body_parser = BodyParser()
def parse_cookies(self, cookies) -> dict[str, str]:
        cookies = [cookie.split("=") for cookie in cookies.split(";")]   
        return {key: value for key, value in cookies}
def parse_request(self, request: str) -> Request:
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
                                "body": None,
                                "cookies": None,
                                "query": None
                            }
        # getting the different parts of the HTTP request: request line, headers, and the body
        req_n_headers, body = request.split("\r\n\r\n", 1)
        request_line, headers = req.split("\r\n", 1)
        headers = headers.split("\r\n")
        
        
        # parsing the first line of the request, that contains the method, the uri (ressource requested) and the protocol
        request_line_parts = request_line.split(" ")
        request_as_object["method"], request_as_object["uri"], request_as_object["protocol"] = request_line_parts
        query_string = ''
        if '?' in uri:
            request_as_object["uri"], query_string = request_as_object["uri"].split("?", 1)
        
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
        else:
            request_as_object["cookies"] = {}
        
        # parsing the body with the body parser only if the method is not GET
        if request_as_object["method"] != "GET":
            body = self.body_parser.parse(body, headers_obj["Content-Type"])
            request_as_object["body"] = body
        else :
            body = {}

        
        # i forgot to parse the url parameters (/books?id=1&name=foo) i will add them later (added them now)
        query_obj = {}
        if query_string:
            query_obj = {query.split("=")[0] : unquote_plus(query.split("=")[1], 'utf8') for query in query_string.split("&")}
        request_as_object["query"] = query_obj
        return Request(method=request_as_object["method"], uri=request_as_object["uri"], protocol=request_as_object["protocol"], headers=request_as_object["headers"], body=request_as_object["body"], cookies=request_as_object["cookies"])
        
        
    
    
        
    
