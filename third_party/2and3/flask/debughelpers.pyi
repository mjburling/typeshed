# Stubs for flask.debughelpers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from ._compat import implements_to_string as implements_to_string, text_type as text_type
from .app import Flask as Flask
from .blueprints import Blueprint as Blueprint
from .globals import _request_ctx_stack as _request_ctx_stack

class UnexpectedUnicodeError(AssertionError, UnicodeError): ...

class DebugFilesKeyError(KeyError, AssertionError):
    msg = ...  # type: Any
    def __init__(self, request, key): ...

class FormDataRoutingRedirect(AssertionError):
    def __init__(self, request): ...

def attach_enctype_error_multidict(request): ...
def explain_template_loading_attempts(app, template, attempts): ...
