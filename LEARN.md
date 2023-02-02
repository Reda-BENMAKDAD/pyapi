# Hello everyone!
> Here i will share with you how i got the idea to make this project, and the steps i followed to make it

## __How i got the idea__
so i was working a lot with frameworks like __*Expressjs*__ and __*Flask*__ because i am a Fullstack developper, and i was really curious about how it works under the hood; how the framework accepts and handles HTTP requests, parses them, maps my routes to my functions, sends a correct response...etc. <br>
of course i had a general idea of how it works, but i wanted to trully get a good grasp of it, so i decided do it my self, and that's how i started making this project

## __Steps i followed making this project__
i wanted to start from __scratch__ , like really from the ground up, so i decided to :

- __Make my own web server with sockets__: i have already worked with sockets in python, so i decided to make my web server with that. the server had to accept connections from client, and handle them simultaniously, i used threads to implement this.
- __make an HTTP request parser__: HTTP protocol follows some strict specifications that you can find [here](https://www.ietf.org/rfc/rfc2616.txt) and that i had to understand to start parsing HTTP requests, (of course i didn't read all of that i just asked chatGPT to summarize it for me). this http request parser handles parsing of the request it self, the url arguments, the body, the headers according to the specifications.
- __make an HTTP response builder__: this thing is supposed to build a valid  HTTP response (again in accordance to the HTTP specifications), so that the user doesn't deal with it

and that's it, these are the components that i needed to stat, i implemented them, it was working, so i pushed it to github and to the community exchange

## Conclusion
I hope that you liked my project and  it helped you understand some HTTP concepts, if you find any issuses or want to improve my code, don't hesitate to contribute by opening issues or pull requests.

# __Thanks for reading!__

