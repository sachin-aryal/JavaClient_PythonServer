#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import  cgi
PORT_NUMBER = 8080


class myHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        print "POST Request......"
        print self.path
        if self.path == "/send":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            try:
                filePath = form["file_path"].value
                print "File Path Received from Client: "+`filePath`
                self.send_response(200)
            except:
                self.send_response(500)
            self.end_headers()
        return


try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    # Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()