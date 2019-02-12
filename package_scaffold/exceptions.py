class Error(Exception):
    """Base class for other exceptions"""
    pass


class DirectoryExistsError(Error):
    """Raised when the directory exists"""
    pass


class ForgottenNameError(Error):
    """Raised when the user fotget pass the name of the project"""
    pass
