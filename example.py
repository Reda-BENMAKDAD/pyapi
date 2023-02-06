# note: this code is heavily commented to help you understand what's going on, don't get afraid lol
from server.server import Server

# we first create our api by instantiating the Server class
api = Server(port=8000, verbose=True)
# now we define our route handlers

# this is the function that handles the "/" route
def root_route(req, res):
    # please look at the README.md file to understand these req and res objects
    res.send("Hello World")

# and we map our route handler to the route
api.get("/", root_route)

# at this point we can already launch the app and test it
# api.start()
# but we will define some other routes for the sake of example

def query_route(req, res):
    # this route returns the uri parameters parameters as a json object
    res.json(req.uri_params)

def book_route(req, res):
    # this route returns a form to the client, to submit a book name
    res.sendFile("./static/books.html")

def books_post_route(req, res):
    # this function handles the form submission from the "/book" route
    book_name = req.body["data"]["bookname"]
    response = f"""<!DOCTYPE html>
<html>
<head></head>
<body>
you entered {book_name} as book name
</body>
</html>"""

    res.send(response)
    
# now we map our route handlers to the routes
api.get("/uri/query", query_route)
api.get("/book", book_route)
api.post("/books", books_post_route)

# and we launch the app
api.start()

