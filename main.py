# main.py

import cgi
import re
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from src.orm import setup_orm, db
from src.models import item
import json


def recently_added(environ, start_response):
    start_response('200 OK', [ ('Content-type', 'text/json'),
                              ('Access-Control-Allow-Origin', '*')])
    session = db()
    #this logic should be moved into a repository script
    #the call should really be ItemsRepo.get_recently_added(limit=16)
    #make sure you filter out deleted items
    results = session().query(item.Item).order_by(item.Item.id.desc()).limit(16).all()
    result = {'results': [r.to_json() for r in results]}
    yield json.dumps(result).encode('utf-8')


def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return [b'Not Found']

# map urls to functions
urls = [
    (r'^$', not_found),
    (r'api/items/recently-added?$', recently_added),
    (r'api/(.+)$', not_found)
]

def application(environ, start_response):
    """
    The main WSGI application. Dispatch the current request to
    the functions from above and store the regular expression
    captures in the WSGI environment as  `myapp.url_args` so that
    the functions from above can access the url placeholders.

    If nothing matches call the `not_found` function.
    """
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)



if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    setup_orm()
    httpd = make_server('', 5000, application)
    print('serving on port 5000')
    httpd.serve_forever()
