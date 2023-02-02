# **PYAPI**
## __Description of the project__
> This is a simple web server built from scratch, to quickly and easily create your APIs. basically I wanted to learn how frameworks like __*Flask*__ and __*Expressjs*__ work (how they handle routes, HTTP parsing, authentification...etc.), so I created my own, with python and the buit-in sockets module.


<br>

## In this package, you'll find the following components:
- A server built with the sockets module
- An HTTP request parser
- An HTTP body parser
- A routes handler that uses threads

## Features i want to add:
- An HTTP response builder (to easily create valid HTTP responses)
- file rendering (because right now i am just sending plain HTML strings)
- middlewares and easy custom middleware integration
- authentification handlers
- database and migrations handling

> you can take a look at these components to understand how i implemented them, and if you have any feedback, suggestions or questions, please feel free to open a discussion or issue on the repository. If you'd like to make improvements, you're welcome to submit a pull request.

<br>

## Try the server
### ___launch the app I made___
to launch the demo server, clone the repository, and run the following commands
```bash
cd pyapi
python3 example.py
```
the server will then be started, you can navigate to http://127.0.0.1:8000/ to see it in action

### ___or create your own app___
to create your own app with this server, you just have to import the server class to your file, and instanciate it, like the following
```python
from server import Server

# the port parameter is optional, by default it will be 8080
api = Server(port=8000)
```

and then you can define routes by making callback functions that will be called when the user vists a route, these functions take two arguments:
1. __req__ : short for request, it's an object that contains all the information of the user's request, (HTTP method, url, headers...). it is made by parsing the HTTP request received from the user with the __request_parser__ class in the __http_utils__ file, and putting all the info in the __Request__ class, and instance of this class is then passed to your function, with all the info about the request
2. __res__ : short for response, this parameter is from which you wil send a response to the user, right now it is just a raw TCP socket it lets you send a manually built response to the client, it will soon be replaced by a __response_builder__ class that will handle the HTTP part for you.

```python
# creating routes for our application

import Server from server
api = Server(port=8000)

# function for the root route "/" 
# that takes the req and res parameters
def root_route(req, res):
    # right now, you have to build the HTTP response manually (specify the protocol, status code, headers...etc) manually
    # but this will be changed to be handled automatically
    res.send("""HTTP/1.1 200 OK


<!DOCTYPE html>
<html>
    <head>
        <title>Welcome to my api</title>
    </head>
    <body>
        <h1>this is my first api with PYAPI</h1>
    </body>
</html>""".encode())

# function for "/foo" route that is a get route
def foo_route(req, res):
    res.send("""HTTP/1.1 200 OK
             
<!DOCTYPE html>
<html>
    <head>
        <title>Welcome to my api | foo</title>
    </head>
    <body>
        <h1>Welcome to the foo route</h1>
    </body>
</html>""".encode())

# function for "/post" route that is a post route
def post_route(req, res):
    username = req.body["data"]["username"]
    res.sendall(f"""HTTP/1.1 200 OK

            
<!DOCTYPE html>
<html>
    <head>
        <title>Welcome to my api | foo</title>
    </head>
    <body>
        <h1>Welcome to the post route, you posted {username} as username</h1>
    </body>
</html>""".encode())


# form route for the username 
def form_route(req, res):
    res.send("""HTTP/1.1 200 OK


<!DOCTYPE html>
<html>
    <head>
        <title>Username form</title>
    </head>
    <body>
        <form method="POST" action="/post">
            <label>username: </label>
            <input type="text" name="username" />
            <input type="submit" value="submit" name="submit" />
        </form>
</html>""".encode())
```

and then you cann add these route handlers to your app
```python

# depending on the method you want to use for the route, 
# you either choose get, post, put...methods

api.get("/", root_route)
api.get("/foo", foo_route)
api.get("/form", form_route)
api.post("/post", post_route)
```
and after defining all your routes, we can start your application

```python
api.start()
```

<br>



<br>

 __*Note:&nbsp;*__ this is just a side-roject, i work on it from time to time, so a LOT of things are not looking good, but i will improve them. thanks for reading!


