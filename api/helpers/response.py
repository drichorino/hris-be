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
        # Error types mapping remains the same...
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
