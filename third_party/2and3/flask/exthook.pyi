# Stubs for flask.exthook (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from ._compat import reraise as reraise

class ExtDeprecationWarning(DeprecationWarning): ...

class ExtensionImporter:
    module_choices = ...  # type: Any
    wrapper_module = ...  # type: Any
    prefix = ...  # type: Any
    prefix_cutoff = ...  # type: Any
    def __init__(self, module_choices, wrapper_module): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def install(self): ...
    def find_module(self, fullname, path=None): ...
    def load_module(self, fullname): ...
    def is_important_traceback(self, important_module, tb): ...
    def is_important_frame(self, important_module, tb): ...
