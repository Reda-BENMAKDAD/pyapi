# **PYAPI**
## __Description of the project__
> This is a simple web server built from scratch, to quickly and easily create your APIs. __to understad the project :__ basically I wanted to learn how frameworks like __*Flask*__ and __*Expressjs*__ work (how they handle routes, HTTP parsing, authentification...etc.), so I created my own, with python and the buit-in sockets module. i hope that my server will help you demistify these frameworks since mine is very simple to understand


<br>

## In this package, you'll find the following components:
- A server built with the sockets module
- An HTTP request parser
- An HTTP body parser
- An HTTP response builder (to easily create valid HTTP responses)
- A routes handler that uses threads


> you can take a look at these components to understand how i implemented them, and if you have any feedback, suggestions or questions, please feel free to open a discussion or issue on the repository. If you'd like to make improvements, you're welcome to submit a pull request.

<br>

## Try the server
### ___launch the app I made___
to launch the demo server, clone the repository, and run the following commands
```bash
cd pyapi
python3 example.py
```
the server will then be started, you can navigate to http://127.0.0.1:8000/ to see it in action, and read the code to understand how it works

### ___or create your own app___
to create your own app with this server, you just have to import the server class to your file, and instanciate it, like the following
```python
from server import Server

# the port parameter is optional, by default it will be 8080
api = Server(port=8000)
```

and then you can define routes by making callback functions that will be called when the user vists a route, these functions take two arguments:
1. __req__ : short for request, it's an class that contains all the information about the user's request, (HTTP method, url, headers...). it is made by parsing the HTTP request received from the user with the __request_parser__ class, and putting all the info in the __Request__ class, it is then passed to your function, with all the info about the request
<br>

2. __res__ : short for response, this parameter is from which you wil send a response to the user, you can use the __*send*__ method to send plain text, html, xml..etc or __*sendfile*__ method to send a file

```python
# creating routes for our application

from server import Server
api = Server(port=8000)

# we should first create route handlers
def root_route(req, res):
    res.send("Hello World")

# and then map the route handler to a route and a method
api.get("/", root_route) 

def post_route(req, res):
    submitted_data = req.body["data"]
    print(submitted_data)

api.post("/post", post_route)
```

and then you cann start your app


```python
api.start()
```

<br>



<br>

 __*Note:&nbsp;*__ this is just a side-roject, i work on it from time to time, so a LOT of things are not looking good, but i will improve them. thanks for reading!


