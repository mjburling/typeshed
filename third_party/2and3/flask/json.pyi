# Stubs for flask.json (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
from typing import Any, IO

import _json
from itsdangerous import simplejson as _json
from itsdangerous import json as _json

class JSONEncoder(_json.JSONEncoder):
    def default(self, o: Any) -> Any: ...

class JSONDecoder(_json.JSONDecoder): ...

def dumps(obj: Any,
    encoding: Any = ...,
    **kwargs: Any) -> Any: ...

def dump(obj: Any,
    fp: IO[str],
    encoding: Any = ...,
    **kwargs: Any) -> None: ...

def loads(s: str,
    **kwargs: Any) -> Any: ...

def load(fp: IO[str],
    **kwargs: Any) -> Any: ...

def htmlsafe_dumps(obj: Any,
    encoding: Any = ...,
    **kwargs: Any) -> Any: ...

def htmlsafe_dump(obj: Any,
    fp: IO[str],
    encoding: Any = ...,
    **kwargs: Any) -> None: ...

def jsonify(*args: Any,
    **kwargs: Any) -> Any: ...