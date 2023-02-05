from pprint import PrettyPrinter
from HTTP.body_parser import BodyParser
from urllib.parse import unquote_plus
from urllib import parse
from HTTP.body_parser import Body

# the class request that will be passed to the user's route handler

pp = PrettyPrinter(indent=4)

class Request:
    
    def __init__(self, method, uri, protocol, uri_params: dict=None, headers: dict=None, cookies: dict=None, body: dict=None):
        self.method = method
        self.uri = uri
        self.protocol = protocol
        self.uri_params = uri_params
        self.headers = headers
        self.cookies = cookies
        self.body = body
        
    def __str__(self):
        return f"""
method: {self.method}
uri: {self.uri}
uri_params: {pp.pformat(self.uri_params)}
protocol: {self.protocol}
headers: {pp.pformat(self.headers)}
body: {pp.pformat(self.body.data)}
"""
        
    
class RequestParser:

    def __init__(self):
        self.bodyParser = BodyParser() # to let user pass a custom body parser
        
    
    def parse(self, request: str) -> None:
        """
        Note: this parsing of the request can go wrong in many ways. it is not fully compliant with the HTTP specifications, 
        but should work for most of the cases.
        if you are comfortable with the HTTP protocol, please do not hesitate to improve this function to meet the specs, thanks!    
        """    
        # getting the different parts of the HTTP request: request line, headers, and the body
        request_headers_body = request.split("\r\n\r\n", 1)
        request_and_headers = request_headers_body[0]
        body_str: str = request_headers_body[1] # body as string from the request
        request_line, headers_str = request_and_headers.split("\r\n", 1) # request line
        headers_lstr = headers_str.split("\r\n") # headers as a list of strings
        
        
        # parsing the first line of the request, that contains the method, the uri (ressource requested), uri params and the protocol
        # TODO: handle errors if the request is malformed (not enough arguments for unpacking etc.)
        method, uri, protocol = request_line.split(" ")
        uri_params: dict = self.parse_url_params(uri)
        
        # parsing the headers part to get a dictionary of headers
        headers: dict = {}
        for header in headers_lstr:
            header_parts = header.split(": ")
            headers[header_parts[0]] = header_parts[1]

        # parsing the cookies in the headers
        cookies: dict = {}
        if "Cookie" in headers:
            cookies = self.parse_cookies(headers["Cookie"])
        
        # parsing the body with the body parser only if the method is not GET
        # TODO: find a good way to parse the body (improve the body parser to take into account the headers) and fit all of the
        # information in the request object
        body: dict = {}
        if method != "GET":
            body = self.bodyParser.parse(body_str, headers)
        else:
            body = Body(body_str, {})
        
        return Request(method=method, uri=uri, protocol=protocol, uri_params=uri_params, headers=headers, cookies=cookies, body=body)
        
    def parse_cookies(self, cookies_str: str) -> dict:
        cookies_str = parse.unquote(cookies_str)
        cookies: dict = {}
        cookies_list = [cookie.strip() for cookie in cookies_str.split(";")]
        for cookie in cookies_list:
            if "=" not in cookie:
                continue
            cookie_parts = cookie.split("=", 1)
            
            if len(cookie_parts) != 2 or cookie_parts[0] == "":
                continue
            else:
                cookies[cookie_parts[0]] = cookie_parts[1]
            
        return cookies

    def parse_url_params(self, url: str) -> dict:
        """
        parses the url parameters and returns a dictionary of the parameters
        """
        url_params: dict = {}
        if "?" not in url:
            return url_params
        url_parts = url.split("?")
        url = url_parts[0]
        params = url_parts[1]
        params = unquote_plus(params)
        params_list = params.split("&")
        for param in params_list:
            param_parts = param.split("=")
            if len(param_parts) != 2:
                continue
            else:
                url_params[param_parts[0]] = param_parts[1]
        return url_params
