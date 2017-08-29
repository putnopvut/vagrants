#!/usr/bin/env python

import socket
import sys
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        return SimpleHTTPRequestHandler.do_GET(self)


class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6


def main():
    print("Running HTTP server on {0}".format(sys.argv[1]))
    server = HTTPServerV6((sys.argv[1], 8000), MyHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
