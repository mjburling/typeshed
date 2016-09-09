# Stubs for flask (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .app import Flask as Flask, Request as Request, Response as Response
from .config import Config as Config
from .helpers import url_for as url_for, flash as flash, send_file as send_file, send_from_directory as send_from_directory, get_flashed_messages as get_flashed_messages, get_template_attribute as get_template_attribute, make_response as make_response, safe_join as safe_join, stream_with_context as stream_with_context
from .globals import current_app as current_app, g as g, request as request, session as session, _request_ctx_stack as _request_ctx_stack, _app_ctx_stack as _app_ctx_stack
from .ctx import has_request_context as has_request_context, has_app_context as has_app_context, after_this_request as after_this_request, copy_current_request_context as copy_current_request_context
from .blueprints import Blueprint as Blueprint
from .templating import render_template as render_template, render_template_string as render_template_string
from .signals import signals_available as signals_available, template_rendered as template_rendered, request_started as request_started, request_finished as request_finished, got_request_exception as got_request_exception, request_tearing_down as request_tearing_down, appcontext_tearing_down as appcontext_tearing_down, appcontext_pushed as appcontext_pushed, appcontext_popped as appcontext_popped, message_flashed as message_flashed, before_render_template as before_render_template
from .sessions import SecureCookieSession as Session

jsonify = ...  # type: Any
json_available = ...  # type: Any