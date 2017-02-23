class TypeFormException(Exception):
    pass


class InvalidRequestException(TypeFormException):
    pass


class NotAuthorizedException(TypeFormException):
    pass


class RateLimitException(TypeFormException):
    pass


class UnknownException(TypeFormException):
    pass


class NotFoundException(TypeFormException):
    pass
