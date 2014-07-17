
class ForbiddenError(StandardError):
    pass


class ErrorTranslation(object):
    def __init__(self, cls, status=500, message=None):
        self.cls = cls
        self.status = status
        self.message = message

    def translate(self, error):
        message = self.message or error.message
        return dict(message=message), self.status

    def applies(self, error):
        return isinstance(error, self.cls)


errors = [
    ErrorTranslation(ForbiddenError, 403),
]


def with_translated_errors(f):
    """Turns exceptions into status codes and nice error messages."""
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except StandardError as e:
            print e
            for err in errors:
                if err.applies(e):
                    return err.translate(e)

            raise
    return wrapper
