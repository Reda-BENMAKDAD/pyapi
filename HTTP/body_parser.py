import json
class body_parser:
    
    def __init__(self):
        pass
    
    def parse(self, body: str, content_type: str) -> dict:
        if body == "":
            return {}
        
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
                return body
            
            
    def parse_text_plain(self, body: str, content_type: str) -> dict:
        return {
            "content_type": content_type,
            "data": body
        }
        
    
    def parse_form_urlencoded(self, body: str, content_type) -> dict:
        body_r  = {
            "content_type": content_type,
            "data": {}
        }
        params_obj = {}
        params = [param.split("=") for param in body.split("&")]
        for param in params:
            key = param[0]
            value = param[1]
            params_obj.update({key: value})
            
        body_r["data"] = params_obj
        return body_r
            
    
    def parse_multipart_form_data(self, body: str, content_type) -> dict:
        pass