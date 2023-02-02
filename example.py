from server.server import Server

# we create our api by inctanciating the Server class
api = Server(port=8000)


# defining route handlers
def root_route(req, res):
    print(req)
    
    res.send("HTTP/1.1 200 OK\r\n\r\n<!DOCTYPE html><html><head></head><body>Hello World,  go to <a href=\"/books\">books route</a></body><html>".encode())
    
    
def books_route(req, res):
    print(req.uri)
    print(req.method)
    res.sendall("HTTP/1.1 200 OK\r\n\r\n<!DOCTYPE html><html><head></head><body>Hello World, welcome to books route <form method=\"POST\" action=\"/books\"><label>enter book name</label><input type=\"text\" name=\"bookname\" /> <input type=\"submit\"/></form></body><html>".encode())


def books_post_route(req, res):
    book_name = req.body["data"]["bookname"]
    response = f"""HTTP/1.1 200 OK


<!DOCTYPE html>
<html>
<head></head>
<body>
you entered {book_name} as book name
</body>
</html>""".encode()
    res.sendall(response)
    

# maping route handlers to routes
api.get("/", root_route)
api.get("/books", books_route)
api.post("/books", books_post_route)

# launching the app
api.start(debug=True)