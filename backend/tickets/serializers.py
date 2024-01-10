from rest_framework import serializers
from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'id', 'title', 'requester', 'description', 'created_at', 
            'modify', 'closed_by', 'solution', 'status'
        ]