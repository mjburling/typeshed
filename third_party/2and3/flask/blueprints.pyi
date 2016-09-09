# Stubs for flask.blueprints (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .helpers import _PackageBoundObject as _PackageBoundObject, _endpoint_from_view_func as _endpoint_from_view_func

class BlueprintSetupState:
    app = ...  # type: Any
    blueprint = ...  # type: Any
    options = ...  # type: Any
    first_registration = ...  # type: Any
    subdomain = ...  # type: Any
    url_prefix = ...  # type: Any
    url_defaults = ...  # type: Any
    def __init__(self, blueprint, app, options, first_registration): ...
    def add_url_rule(self, rule, endpoint=None, view_func=None, **options): ...

class Blueprint(_PackageBoundObject):
    warn_on_modifications = ...  # type: Any
    name = ...  # type: Any
    url_prefix = ...  # type: Any
    subdomain = ...  # type: Any
    static_folder = ...  # type: Any
    static_url_path = ...  # type: Any
    deferred_functions = ...  # type: Any
    url_values_defaults = ...  # type: Any
    def __init__(self, name, import_name, static_folder=None, static_url_path=None, template_folder=None, url_prefix=None, subdomain=None, url_defaults=None, root_path=None): ...
    def record(self, func): ...
    def record_once(self, func): ...
    def make_setup_state(self, app, options, first_registration=False): ...
    def register(self, app, options, first_registration=False): ...
    def route(self, rule, **options): ...
    def add_url_rule(self, rule, endpoint=None, view_func=None, **options): ...
    def endpoint(self, endpoint): ...
    def app_template_filter(self, name=None): ...
    def add_app_template_filter(self, f, name=None): ...
    def app_template_test(self, name=None): ...
    def add_app_template_test(self, f, name=None): ...
    def app_template_global(self, name=None): ...
    def add_app_template_global(self, f, name=None): ...
    def before_request(self, f): ...
    def before_app_request(self, f): ...
    def before_app_first_request(self, f): ...
    def after_request(self, f): ...
    def after_app_request(self, f): ...
    def teardown_request(self, f): ...
    def teardown_app_request(self, f): ...
    def context_processor(self, f): ...
    def app_context_processor(self, f): ...
    def app_errorhandler(self, code): ...
    def url_value_preprocessor(self, f): ...
    def url_defaults(self, f): ...
    def app_url_value_preprocessor(self, f): ...
    def app_url_defaults(self, f): ...
    def errorhandler(self, code_or_exception): ...
    def register_error_handler(self, code_or_exception, f): ...