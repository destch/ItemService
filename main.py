# main.py

import cgi
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, String, Integer
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
metadata = Base.metadata
engine = create_engine('postgresql://danielchavez:daniel97@ec2-34-198-0-244.compute-1.amazonaws.com/ClothDB_DEV')

item_table = Table(
    'items', metadata,
    Column('name', Integer)
)

DBSession = sessionmaker(bind=engine)
session = DBSession()
results = session.query(item_table).limit(10).all()
print(results)



def notfound_404(environ, start_response):
    start_response('404 not found', [ ('Content-type', 'text/plain') ])
    return [b'Not Found']

class PathDispatcher:
    def __init__(self):
        self.pathmap = {

        }

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'],
                                  environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = { key: params.getvalue(key) for key in params }
        handler = self.pathmap.get((method, path), notfound_404)
        return handler(environ, start_response)

    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        return function

def test(environ, start_response):
    start_response('200 OK', [ ('Content-type', 'text/json') ])
    params = environ['params']
    _hello_resp = "<html><h1>Hello {name}</h1></html>"
    resp = _hello_resp.format(name=params.get('name'))
    yield resp.encode('utf-8')

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/', test)

    httpd = make_server('', 3000, dispatcher)
    print('serving on port 3000')
    httpd.serve_forever()
