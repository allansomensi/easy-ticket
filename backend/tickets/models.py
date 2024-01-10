from django.db import models
from users.models import UserProfile

STATUS_CHOICES = (
    ('ABERTO', 'Em aberto'),
    ('ANDAMENTO', 'Em andamento'),
    ('CONCLUIDO', 'Concluído')
)

PRIORITY_CHOICES = (
    ('BAIXA', 'Baixa'),
    ('MEDIA', 'Média'),
    ('ALTA', 'Alta')
)


class Ticket(models.Model):
    """
    Classe representando o ticket
    """

    # Título do ticket
    title = models.CharField(max_length=30)
    # Descrição do ticket
    description = models.TextField(max_length=800)
    # Requisitante (Usuário)
    requester = models.ForeignKey(
        UserProfile, on_delete=models.PROTECT, related_name='tickets')
    # Data de criação
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    # Data de conclusão
    closed_at = models.DateTimeField(max_length=30, null=True, blank=True)
    # Última modificação
    modify = models.DateTimeField(auto_now=True)
    # Prioridade do ticket
    priority = models.CharField(
        max_length=50, choices=PRIORITY_CHOICES, default='BAIXA')
    # Tags atribuídas
    tags = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    # Avaliação do usuário ao atendimento
    feedback = models.CharField(
        max_length=5, default=None, null=True, blank=True)
    # Origem ticket (Email, Telefone, etc.)
    origin = models.CharField(max_length=30, null=True, blank=True)
    # Quem concluiu o ticket
    closed_by = models.ForeignKey(
        UserProfile, on_delete=models.PROTECT, related_name='closed_by',
        null=True, blank=True)
    # Solução do problema, o que foi feito para resolver.
    solution = models.TextField(
        max_length=800, default=None, null=True, blank=True)
    # Status do ticket (Em aberto, Em andamento ou Concluído)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='ABERTO')

    class Meta:
        ordering = ['status']

    def __str__(self):
        return self.title
