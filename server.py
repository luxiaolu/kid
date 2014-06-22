from wsgiref.simple_server import make_server
from app import app

httpd = make_server('', 8000, app)
print "Serving HTTP on port 8000..."
print "Ctrl+c to stop..."
httpd.serve_forever()
