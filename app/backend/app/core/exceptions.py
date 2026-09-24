class AppError(Exception):
    """Base for domain errors the API layer translates into HTTP responses."""

    status_code = 400
    default_message = "Something went wrong"

    def __init__(self, message: str | None = None):
        super().__init__(message or self.default_message)
        self.message = message or self.default_message


class EmailAlreadyRegisteredError(AppError):
    status_code = 409
    default_message = "An account with this email already exists"


class UsernameTakenError(AppError):
    status_code = 409
    default_message = "This username is already taken"


class InvalidCredentialsError(AppError):
    status_code = 401
    default_message = "Invalid email/username or password"


class NotAuthenticatedError(AppError):
    status_code = 401
    default_message = "Not authenticated"


class NotFoundError(AppError):
    status_code = 404
    default_message = "Not found"
