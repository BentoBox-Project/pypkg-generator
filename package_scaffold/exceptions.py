"""Custom Exceptions for this project.
"""


class Error(Exception):
    """Base class for other exceptions"""


class DirectoryExistsError(Error):
    """Raised when the directory exists"""


class ForgottenNameError(Error):
    """Raised when the user fotget pass the name of the project"""
