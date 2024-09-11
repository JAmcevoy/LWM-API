from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)

@api_view()
def root_route(request):
    """
    Root route for the API.

    - GET: Returns a welcome message.
    """
    return Response({
        "message": "Welcome to my DRF API!"
    })

@api_view(['POST'])
def logout_route(request):
    """
    Handle user logout by clearing JWT cookies.

    - POST: Clears JWT authentication cookies to log out the user.
    """
    response = Response()
    # Clear the access token cookie
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    # Clear the refresh token cookie
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
