from .exceptions import (
    BaseError,
    InternalServerError,
    MethodNotAllowed,
    NotFound,
    StatusCode,
)


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(_):
        return NotFound().to_response()

    @app.errorhandler(405)
    def not_allowed(_):
        return MethodNotAllowed().to_response()

    @app.errorhandler(BaseError)
    def handle_error(error: BaseError):
        from main.libs.log import get_logger

        logger = get_logger(__name__)

        status_code = error.status_code
        if (
            isinstance(status_code, int)
            and status_code != StatusCode.INTERNAL_SERVER_ERROR
        ):
            logging_method = logger.warning
        else:
            logging_method = logger.error

        logging_method(
            error.error_message,
            data={
                "error_data": error.error_data,
                "error_code": error.error_code,
            },
        )
        return error.to_response()

    @app.errorhandler(Exception)
    def handle_exception(e):
        from main.libs.log import get_logger

        logger = get_logger(__name__)
        logger.exception(str(e))

        return InternalServerError(error_message=str(e)).to_response()
