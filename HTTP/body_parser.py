import json
from urllib import parse

class Body:
    
    def __init__(self, content_type: str=None, data: dict={}):
        self.content_type = content_type
        self.data = data


class BodyParser:  
    def parse(self, body: str, content_type: str) -> dict:
        if body == "":
            return Body(content_type, {})
        
        if content_type == None:
            content_type = "text/plain"
            
        
        # depending on the content type, the body will be parsed differently:
        match content_type:
            case "text/plain":
                return self.parse_text_plain(body, content_type)
            case "application/x-www-form-urlencoded":
                return self.parse_form_urlencoded(body, content_type)
            case "multipart/form-data":
                self.parse_multipart_form_data(body, content_type)
            case "application/json":
                return {"content_type": content_type, "data": json.loads(body)}
            case _:
                return Body(content_type, {})
            
            
    def parse_text_plain(self, body: str, content_type: str) -> Body:
        return Body(content_type, body)
        
    
    def parse_form_urlencoded(self, body: str, content_type: str) -> Body:
        body = parse.unquote(body)
        params_obj = {}
        params = [param.split("=") for param in body.split("&")]
        for param in params:
            key = param[0]
            value = param[1]
            params_obj.update({key: value})
            
        return Body(content_type, params_obj)
            
    
    def parse_multipart_form_data(self, body: str, content_type) -> dict:
        pass
