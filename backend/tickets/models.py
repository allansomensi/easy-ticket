from django.db import models
from users.models import UserProfile

STATUS_CHOICES = (
    ('ABERTO', 'Em aberto'),
    ('ANDAMENTO', 'Em andamento'),
    ('CONCLUIDO', 'Concluído')
)


class Ticket(models.Model):
    """Classe representando o ticket"""

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=800)
    requester = models.ForeignKey(
        UserProfile, on_delete=models.PROTECT, related_name='tickets')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
    closed_by = models.ForeignKey(
        UserProfile, on_delete=models.PROTECT, related_name='closed_by', null=True, blank=True)
    solution = models.TextField(
        max_length=800, default=None, null=True, blank=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='ABERTO')

    @property
    def is_closed(self):
        return self.status == 'CONCLUIDO'

    def get_status_display(self):
        return dict(STATUS_CHOICES)[self.status]

    class Meta:
        ordering = ['status']

    def __str__(self):
        return self.title
