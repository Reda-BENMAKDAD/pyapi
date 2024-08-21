# **PYAPI**
## __Description of the project__
> This is a simple web server built from scratch, to quickly and easily create your APIs. __to understad the project :__ basically I wanted to learn how frameworks like __*Flask*__ and __*Expressjs*__ work (how they handle routing, HTTP parsing, connections...etc.), so I created my own Framework, with python and the built-in sockets module. I hope that my server will help you demistify these frameworks since mine is very simple to understand


<br>

## In this package, you'll find the following components:
- An HTTP server built with sockets from scratch
- An HTTP request parser
- An HTTP body parser
- An HTTP response builder (to easily create valid HTTP responses)
- A routes handler that uses threads


> You can take a look at these components to understand how I implemented them, and if you have any feedback, suggestions or questions, please feel free to open a discussion or issue on the repository. If you'd like to make improvements, you're welcome to submit a pull request.

<br>

## Try the server
### ___Launch the app I made___
To launch the demo server, clone the repository, and run the following commands.
```bash
cd pyapi
python3 example.py
```
The server will then be started, you can navigate to http://127.0.0.1:8000/ to see it in action, and read the code to understand how it works.

### ___Or create your own app___
To create your own app with this server, you just have to import the server class to your file, and instanciate it, like the following.
```python
from server import Server

# The port parameter is optional, by default it will be 8000
api = Server(port=8000)
```

Then you can define routes by making callback functions that will be called when the user vists a route, these functions take two arguments:
1. __req__ : short for request, it's a class that contains all the information about the user's request, (HTTP method, url, headers...). It is made by parsing the HTTP request received from the user with the __request_parser__ class, and putting all the info in the __Request__ class, it is then passed to your function, with all the info about the request.
<br>

2. __res__ : short for response, this parameter is from which you wil send a response to the user, you can use the __*send*__ method to send plain text, html, xml..etc or __*sendfile*__ method to send a file.

```python
# Creating routes for our application

from server import Server
api = Server(port=8000)

# We should first create route handlers
def root_route(req, res):
    res.send("Hello World")

# And then map the route handler to a route and a method
api.get("/", root_route) 

def post_route(req, res):
    submitted_data = req.body["data"]
    print(submitted_data)

api.post("/post", post_route)
```

Then you cann start your app.


```python
api.start()
```

<br>



<br>

 __*Note:&nbsp;*__ this is just a side-roject, i work on it from time to time, so a LOT of things are not looking good, but i will improve them. thanks for reading!


