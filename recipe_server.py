from http.server import BaseHTTPRequestHandler, HTTPServer
from controllers.blog_controller import *
from response_message.responses import Response
import sys
import re


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        if re.match('/blog/\d+$', self.path):
            record = BlogController.get_blog(self)
            if record:
                Response.response_200(self, record, 'application/json')
            else:
                Response.response_400(self)

        elif re.match('/blog$', self.path):
            record = BlogController.list_blogs()
            if record:
                Response.response_200(self, record, 'application/json')
            else:
                Response.response_400(self)

        else:
            Response.response_400(self, response_message='url scheme does not match')

    def do_POST(self):
        if re.match('/blog/\d+$', self.path):
            response_message = BlogController.add_blog(self)
            if not response_message:
                Response.response_200(self, 'Record added successfully', 'text/plain')
            elif 'Authentication' in response_message:
                Response.response_401(self, response_message)
            else:
                Response.response_409(self, response_message)

        else:
            Response.response_400(self, response_message='url scheme does not match')

    def do_DELETE(self):
        if re.match('/blog/\d+$', self.path):
            response_message = BlogController.del_blog(self)
            if not response_message:
                Response.response_200(self, 'Record deleted', 'text/plain')
            elif 'Authentication' in response_message:
                Response.response_401(self, response_message)
            else:
                Response.response_409(self, response_message)

        else:
            Response.response_400(self, response_message='url scheme does not match')

    def do_PUT(self):
        if re.match('/blog/\d+$', self.path):
            response_message = BlogController.update_blog(self)
            if not response_message:
                Response.response_200(self, 'Record Updated', 'text/plain')
            elif 'Authentication' in response_message:
                Response.response_401(self, response_message)
            else:
                Response.response_409(self, response_message)

        else:
            Response.response_400(self, response_message='url scheme does not match')


if __name__ == '__main__':
    hostName = "0.0.0.0"
    hostPort = 80
    sys.stderr.write('server started')
    myServer = HTTPServer((hostName, hostPort), MyServer)
    myServer.serve_forever()

