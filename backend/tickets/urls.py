from django.urls import path
from . import views

urlpatterns = [
    path(
        'tickets/', views.TicketListCreateView.as_view(),
        name='tickets-list-create'
    ),
    path(
        'tickets/<int:pk>/', views.TicketRetrieveUpdateDestroyView.as_view(),
        name='tickets-detail'
    ),
]
