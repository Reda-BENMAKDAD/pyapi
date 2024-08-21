# note: this code is heavily commented to help you understand what's going on, don't be afraid lol
from server.server import Server

# we first create our api by instantiating the Server class
api = Server(port=8000, verbose=True)

# now we define our route handlers
# this is the function that handles the "/" route
@api.get("/")
def root_route(req, res):
    # please look at the README.md file to understand the req and res parameters
    res.sendFile("./static/index.html")


# at this point we can already launch the api and test it
# api.start()
# but we will define some other routes for the sake of example
@api.get("/query")
def query_route(req, res):
    # this route returns the uri parameters as a json object
    res.json(req.uri_params)

@api.get("/book")
def book_route(req, res):
    # this route returns a form to the client, to submit a book name
    res.sendFile("./static/book.html")

# @api.get("/book")
# def book_route(req, res):
#     res.("hello")

@api.post("/book")
def books_post_route(req, res):
    # this function handles the form submission from the "/book" route
    book_name = req.body.data["bookname"]
    response = f"""<!DOCTYPE html>
<html>
<head></head>
<body>
you entered <span style="color:blue">{book_name}</span> as book name
</body>
</html>"""

    res.send(response)

# and we launch the app
api.start()

