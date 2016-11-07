class PyCardPayException(Exception):
    """Base PyCardPay exception."""
    pass


class XMLParsingError(PyCardPayException):
    """Raised when lxml failed to parse xml from string"""
    pass


class HTTPError(PyCardPayException):
    """Raised when requests.Response.response_code contains value other than 2xx"""
    pass