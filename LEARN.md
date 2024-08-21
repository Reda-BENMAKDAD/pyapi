# Hello everyone!
> Here I will share with you how i got the idea to make this project and the steps I followed to make it

## __How I got the idea__
So I was working a lot with frameworks like __*Expressjs*__ and __*Flask*__ because I am a Fullstack developper, and I was really curious about how it works under the hood; how the framework accepts and handles HTTP requests, parses them, maps my routes to my functions, sends a correct response...etc. <br>
Of course I had a general idea of how it works, but I wanted to truly get a good grasp of it, so I decided do it my self, and that's how I started making this project.

## __Steps I followed making this project__
I wanted to start from __scratch__ , like really from the ground up, so I decided to:

- __Make my own web server with sockets__: I have already worked with sockets in python, so I decided to make my web server with that. The server had to accept connections from client, and handle them simultaniously, I used threads to implement this.
- __Make an HTTP request parser__: HTTP protocol follows some strict specifications that you can find [here](https://www.ietf.org/rfc/rfc2616.txt) and that I had to understand to start parsing HTTP requests, (of course I didn't read all of that I just asked ChatGPT to summarize it for me). This http request parser handles parsing of the request it self, the url arguments, the body, the headers according to the specifications.
- __Make an HTTP response builder__: This thing is supposed to build a valid  HTTP response (again in accordance to the HTTP specifications), so that the user doesn't deal with it.

And that's it, these are the components that I needed to stat, I implemented them, it was working, so I pushed it to github and to the community exchange

## Conclusion
I hope that you liked my project and it helped you understand some HTTP concepts, if you find any issuses or want to improve my code, don't hesitate to contribute by opening issues or pull requests.

# __Thanks for reading!__

