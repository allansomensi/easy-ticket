from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.TicketListCreateView.as_view(), name='tickets-list-create'),  # noqa: E501
    path('tickets/<int:pk>/', views.TicketRetrieveUpdateDestroyView.as_view(), name='tickets-detail'),  # noqa: E501
]
