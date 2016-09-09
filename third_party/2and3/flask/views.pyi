# Stubs for flask.views (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .globals import request as request
from ._compat import with_metaclass as with_metaclass

http_method_funcs = ...  # type: Any

class View:
    methods = ...  # type: Any
    decorators = ...  # type: Any
    def dispatch_request(self): ...
    @classmethod
    def as_view(cls, name, *class_args, **class_kwargs): ...

class MethodViewType(type):
    def __new__(cls, name, bases, d): ...

class MethodView:
    def dispatch_request(self, *args, **kwargs): ...