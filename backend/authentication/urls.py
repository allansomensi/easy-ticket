from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView  # noqa: E501


urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # noqa: E501
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # noqa: E501
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # noqa: E501
]
