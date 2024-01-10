from django.urls import path
from . import views

urlpatterns = [

    path('users/', views.UserListCreateView.as_view(), name='users-list-create'),  # noqa: E501
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='users-detail'),  # noqa: E501
]
