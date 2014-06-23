class WSGIApplication(object):
    
    def __init__(self):
        self.request = None
        self.responce_callback = None

        self.responce_func_dic = {}

    def add_func(self, request_key, responce_func):
        self.responce_func_dic[request_key] = responce_func

    def responce(self):
        request_key = (method, path) = (self.request['REQUEST_METHOD'],
                                        self.request['PATH_INFO'])
        if request_key in self.responce_func_dic:
            responce_func = self.responce_func_dic[request_key] 
            return responce_func()
        else:
            return "server error"

    def get_wsgi_application(self):
        def wsgi(env, start_responce):
            self.request = env
            self.responce_callback = start_responce
            self.responce_callback('200 OK', [('Contend-Type', 'text/html')])
            return self.responce()
        return wsgi

    def run(self, port=8000, host='127.0.0.1'):
        """
        just for test purpose
        """
        from wsgiref.simple_server import make_server
        server = make_server(host, port, self.get_wsgi_application())
        server.serve_forever()

def get(path):
    def __de(f):
        wsgi_app.add_func(('GET',path), f)
        def _(*args, **kargs):
            f(*args, **kargs)
        return _
    return __de

def post(path):
    def __de(f):
        wsgi_app.add_func(('POST',path), f)
        def _(*args, **kargs):
            f(*args, **kargs)
        return _
    return __de
    

wsgi_app = WSGIApplication()
if __name__ == "__main__":
    wsgi_app.run()
else:
    application = wsgi_app.get_wsgi_application()
