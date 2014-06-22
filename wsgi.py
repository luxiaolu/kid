class WSGIApplication(object):
    
    def __init__(self):
        self.request_obj = None
        self.responce_callback = None

        self.responce_func_dic = {}

    def add_func(self, request_key, responce_func):
        self.responce_func_dic[request_key] = responce_func

    def responce(self):
        request_key = (method, path) = (self.request['REQUEST_METHOD'],
                                        self.request['PATH_INFO'])
        if request_key in self.responce_func_dic:
            responce_func = self.responce_func_dic[request_key]() 
            self.responce_callback('200 OK', [('Contend-Type', 'text/html')])
            responce_func()
        else:
            return "server error"


    def get_wsgi_application(self):
        def wsgi(env, start_responce):
            self.request_obj = env
            self.reponce_callback = start_responce
            self.responce()
        return wsgi

    def run(self, port=8000, host='127.0.0.1'):
        """
        just for test purpose
        """
        from wsgiref.simple_server import make_server
        server = make_server(host, port, self.get_wsgi_application())
        server.serve_forever()


wsgi_app = WSGIApplication()
if __name__ == "__main__":
    wsgi_app.run()
else:
    application = wsgi.get_wsgi_application()
