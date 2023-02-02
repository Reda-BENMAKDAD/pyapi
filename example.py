from server.server import Server

# we create our api by inctanciating the Server class
api = Server(port=8000)

# defining route handlers
def root_route(req, res):
    # this is a simple route handler that takes in:
    # [+] a "req" parameter: it's simply a class that groupes all the information that you received from the client
    #                         including the HTTP method used, uri, protocol, headers, cookies, body, body parameters...etc
    #                         you can print the request object to see all the information
    print(req)
    #
    # [+] a "res" parameter: this is what you will use to send your response to the client, you can send plain text, html, xml...
    #                        with the res.send method, or send an entire file with the res.sendfile method
    
    # i will later implement methods in the res class to send json, images...etc
    res.send("<!DOCTYPE html><html><head></head><body>Hello World,  go to <a href=\"/books\">books route</a></body><html>")
    

def foo_route(req, res):
    res.send("Foo route")

def books_route(req, res):
    # this is a route that returns a form to enter a book name, and post it to "/books" route
    res.send("<!DOCTYPE html><html><head></head><body>Hello World, welcome to books route <form method=\"POST\" action=\"/books\"><label>enter book name</label><input type=\"text\" name=\"bookname\" /> <input type=\"submit\"/></form></body><html>")


def books_post_route(req, res):
    # this is the function that handles the POST to the "/books" route
    # retrieving the submitted book name from the request:
    book_name = req.body["data"]["bookname"]
    response = f"""<!DOCTYPE html>
<html>
<head></head>
<body>
you entered {book_name} as book name
</body>
</html>"""

    res.send(response)
    

# maping route handlers to routes
api.get("/", root_route)
api.get("/foo", foo_route)
api.get("/books", books_route)
api.post("/books", books_post_route)

# launching the app
api.start(debug=True)