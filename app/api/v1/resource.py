from flask.ext.restful import Resource as RESTResource
from flask import request
from functools import wraps
import dateutil

from lib.dictify import dictify
from errors import with_translated_errors, ForbiddenError
import authorization

##
# Resource method decorators
#
# Each of these can be wrapped around a resource method. Most are by
# default (see list at end of file)
##


def requires_role(role):
    """Throws a 403:Forbidden error if the requester does not fulfill the
    correct role.

    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if authorization.fulfills_role(role):
                return f(*args, **kwargs)
            else:
                raise ForbiddenError("You must be a %s to do that." % role)
        return wrapper
    return decorator


def return_dict(f):
    """Allows resource methods to return models, lists of models, and
    nested dicts including models; calls public_dict() on all objects
    that provide it.

    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        return dictify(f(*args, **kwargs))
    return wrapper


def extend_with_args(f):
    """Moves get/post arguments into the arg list."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.get_json():
            kwargs.update(request.get_json())

        # WARNING: This may get us into trouble when it comes to
        # list-style "get" args.
        kwargs.update({k: v for k, v in request.args.iteritems()})

        # "auth" is special -- it's an authentication token, not an
        # argument.
        if "auth" in kwargs:
            kwargs.pop("auth")

        # This is JUST for the 1.0 sidebar app.
        if "access_token" in kwargs:
            kwargs.pop("access_token")

        return f(*args, **kwargs)
    return wrapper


class Resource(RESTResource):
    method_decorators = RESTResource.method_decorators + [
        return_dict,
        extend_with_args,
        with_translated_errors
    ]

    def parse_date(self, date_str):
        dt = dateutil.parser.parse(date_str, fuzzy=True)
        return dt.replace(tzinfo=dateutil.tz.tzutc())

    def current_user(self):
        return authorization.current_user()
