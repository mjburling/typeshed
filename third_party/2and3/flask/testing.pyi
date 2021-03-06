# Stubs for flask.testing (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from werkzeug.test import Client
from urlparse import urlsplit as url_parse

def make_test_environ_builder(app, path='', base_url=None, *args, **kwargs): ...

class FlaskClient(Client):
    preserve_context = ...  # type: Any
    def session_transaction(self, *args, **kwargs): ...
    def open(self, *args, **kwargs): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, tb): ...
