from rest_framework import status
from helpers.response import success_response, error_response
from rest_framework.exceptions import ValidationError

class AccountResponseMixin:
    """
    Mixin to use custom response helpers in DRF viewsets.
    """

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return success_response(data=response.data, message="List retrieved successfully.")

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return success_response(data=response.data, message="Account created successfully.", status_code=status.HTTP_201_CREATED)
        except ValidationError as e:
            return error_response(message=e.detail, error_type="validation_error", status_code=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return error_response(str(e), error_type="server_error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return success_response(data=response.data, message="Account retrieved successfully.")

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return success_response(data=response.data, message="Account updated successfully.")
        except ValidationError as e:
            return error_response(message=e.detail, error_type="validation_error", status_code=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return error_response(str(e), error_type="server_error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return success_response(data=None, message="Account deleted successfully.", status_code=response.status_code)
