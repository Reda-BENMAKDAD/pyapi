# **PYAPI**
## __Description of the project__
> This is a simple web server built from scratch, to quickly and easily create your APIs. basically I wanted to learn how frameworks like __*Flask*__ and __*Expressjs*__ work (how they handle routes, HTTP parsing, authentification...etc.), so I created my own, with python and the buit-in sockets module.


<br>

## In this package, you'll find the following components:
- A server built with the sockets module
- An HTTP request parser
- An HTTP response builder
- A routes handler that uses threads

## Features i want to add:
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
the server will then be started, you can navigate to http://127.0.0.1:8888/ to see it in action

### ___or create your own app___
to create your own app with this server, you just have to import the server class to your file, and instanciate it, like the following
```python
from server import Server

# the port parameter is optional, by default it will be 8080
app = Server(port=8000)
```

and then you can define routes, by making callback functions that will be called when the user vists a route, these functions take two arguments:
1. __req__ : short for request, it's an object that contains all the information of the user's request, (HTTP method, url, headers...). it is made by parsing the HTTP request received from the user with the __request_parser__ class in the __http_utils__ file, and putting all the info in the __Request__ class, and instance of this class is then passed to your function, with all the info about the request
2. __res__ : short for response, this parameter is from which you wil send a response to the user, it lets build a response for the user (build the headers, cookies...), and then send it, or send a file directly.

```python
# creating routes for our application

import Server from server
app = Server(port=8000)

# function for the root route "/" 
# that takes the req and res parameters
def root_route(req, res):

    res.send("""<DOCTYPE! html>
<html>
    <head>
        <title>Welcome to my api</title>
    </head>
    <body>
        <h1>this is my first api with PYAPI</h1>
    </body>
</html>
    """)

# function for "/foo" route that is a get route
def foo_route(req, res):
    res.send("""<DOCTYPE! html>
<html>
    <head>
        <title>Welcome to my api | foo</title>
    </head>
    <body>
        <h1>Welcome to the foo route</h1>
    </body>
</html>
    """)

# function for "/post" route that is a post route
def post_route(req, res):
    username = req.body.username
    res.send(f"""<DOCTYPE! html>
<html>
    <head>
        <title>Welcome to my api | foo</title>
    </head>
    <body>
        <h1>Welcome to the post route, you posted {username} as username</h1>
    </body>
</html>
    """)


# form route for the username 
def form_route(req, res):
    res.send("""<!DOCTYPE html>
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
</html>
    """)
```

and then you cann add your routes to your app
```python

# depending on the method you want to use for the route, 
# you either choose get, post, put...methods

app.get("/", root_route)
app.get("/foo", foo_route)
app.get("/form", form_route)
app.post("/post", post_route)
```
and after defining all your routes, we can start your application

```python
app.start()
```

<br>



<br>

 __*Note:&nbsp;*__ this is just a side-roject, i work on it from time to time, so a LOT of things are not looking good, but i will improve them. thanks for reading!


