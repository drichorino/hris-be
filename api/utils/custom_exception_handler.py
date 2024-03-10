from rest_framework.views import exception_handler
from helpers.response import error_response 

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        message = response.data.get('detail', str(exc))

        status_code = response.status_code
        error_type = "unknown_error"

        error_type_map = {
            400: "validation_error",
            401: "unauthorized",
            403: "forbidden",
            404: "not_found",
            405: "method_not_allowed",
            409: "conflict",
            429: "rate_limit_exceeded",
            500: "server_error"
        }
        error_type = error_type_map.get(response.status_code, "unknown_error")
            
        ### More detailed error response
        error_details = response.data if isinstance(response.data, dict) else {'detail': str(exc)}

        return error_response(message=message, error_type=error_type, status_code=status_code)
    return error_response(message=str(exc), error_type="server_error", status_code=500)
