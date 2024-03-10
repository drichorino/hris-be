from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from helpers.response import success_response, error_response


class AuthView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny,]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsAuthenticated,]
        return super().get_permissions()

    # Login
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return error_response("Both username and password are required.", error_type="validation_error")

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                refresh = RefreshToken.for_user(user)
                return success_response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, "Login successful")
            else:
                return error_response("This account is inactive.", error_type="forbidden")
        return error_response("Invalid credentials provided.", error_type="unauthorized")

    # Logout
    def delete(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return success_response(None, "Logout successful.")
        except Exception as e:
            return error_response(str(e), error_type="server_error")
