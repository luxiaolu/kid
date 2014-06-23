from wsgi import get, post, wsgi_app

@get("/")
def test():
    return "<h1>hello kid</h1>"

wsgi_app.run()
