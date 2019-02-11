class Error(Exception):
    """Base class for other exceptions"""
    pass


class DirectoryExistsError(Error):
    """Raised when the directory exists"""
    pass
