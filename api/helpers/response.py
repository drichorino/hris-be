from rest_framework.response import Response
from rest_framework import status


def success_response(data, message="Request successful", status_code=status.HTTP_200_OK):
    return Response({
        'success': True,
        'message': message,
        'data': data
    }, status=status_code)


def error_response(message, error_type="validation_error", status_code=status.HTTP_400_BAD_REQUEST):
    error_types = {
        "validation_error": status.HTTP_400_BAD_REQUEST,
        "unauthorized": status.HTTP_401_UNAUTHORIZED,
        "forbidden": status.HTTP_403_FORBIDDEN,
        "not_found": status.HTTP_404_NOT_FOUND,
        "conflict": status.HTTP_409_CONFLICT,
        "rate_limit_exceeded": status.HTTP_429_TOO_MANY_REQUESTS,
        "server_error": status.HTTP_500_INTERNAL_SERVER_ERROR,
    }
    response_status = error_types.get(error_type, status_code)    
    
    response_data = {
        'success': False,
        'message': {},
    }

    if isinstance(message, dict) or isinstance(message, list):
        response_data['message'] = message
    else:
        response_data['message']['detail'] = message

    return Response(response_data, status=response_status)
