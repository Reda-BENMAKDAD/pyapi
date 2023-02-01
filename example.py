from server.server import Server

api = Server(port=8000)

def root_handler(conn, request):
    print(request)
    
    conn.send("HTTP/1.1 200 OK\r\n\r\n<!DOCTYPE html><html><head></head><body>Hello World <a href=\"/books\">books route</a></body><html>".encode())
    conn.close()
    
api.get("/", root_handler)

api.start(debug=True)