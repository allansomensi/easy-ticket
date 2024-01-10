from django.contrib.auth.models import AbstractUser
from django.db import models

SECTOR_CHOICES = (
    ('ALMOXARIFADO', 'Almoxarifado'),
    ('BALANCA', 'Balança'),
    ('COMERCIAL', 'Comercial'),
    ('COMPRAS', 'Compras'),
    ('CONTABILIDADE', 'Contabilidade'),
    ('CUSTOS', 'Custos'),
    ('DIRETORIA', 'Diretoria'),
    ('ENGENHARIA', 'Engenharia'),
    ('EXPEDICAO', 'Expedição'),
    ('FINANCEIRO', 'Financeiro'),
    ('FUNDICAO', 'Fundição'),
    ('LAB_METALURGICO', 'Laboratório Metalúrgico'),
    ('LAB_METROLOGICO', 'Laboratório Metrológico'),
    ('MANUTENCAO', 'Manutenção'),
    ('PCP', 'PCP'),
    ('PRESET', 'Preset'),
    ('QUALIDADE', 'Qualidade'),
    ('RH', 'RH'),
    ('REBARBACAO', 'Rebarbação'),
    ('RECEBIMENTO', 'Recebimento'),
    ('RECEPCAO', 'Recepção'),
    ('SESMT', 'SESMT'),
    ('TI', 'TI'),
    ('USINAGEM', 'Usinagem'),
)

GENDER_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
)

POSITION_CHOICES = (
    ('ANALISTA', 'Analista'),
    ('DESENVOLVEDOR', 'Desenvolvedor'),
    ('GERENTE', 'Gerente'),
    ('DIRETOR', 'Diretor'),
    ('ESTAGIARIO', 'Estagiário'),
    ('CONTROLLER', 'Controller'),
    ('COORDENADOR_COMPRAS', 'Coordenador de Compras'),
    ('COORDENADOR_LOGISTICA', 'Coordenador de Logística'),
    ('COORDENADOR_ENGENHARIA', 'Coordenador de Engenharia'),
    ('COORDENADOR_VENDAS', 'Coordenador de Vendas'),
)

PERIOD_CHOICES = (
    ('DIURNO', 'Diurno'),
    ('NOTURNO', 'Noturno'),
    ('NAO_APLICAVEL', 'Não aplicável'),
)

NOTIFICATION_PREFERENCE_CHOICES = (
    ('DESATIVADO', 'Desativado'),
    ('SITE', 'Site'),
    ('EMAIL', 'Email'),
)

THEME_CHOICES = (
    ('AUTO', 'Automático'),
    ('LIGHT', 'Modo Claro'),
    ('DARK', 'Modo Escuro'),
)

LANGUAGE_PREFERENCE = (
    ('PT-BR', 'Português do Brasil'),
    ('PT-PT', 'Português de Portugal'),
    ('EN-US', 'Inglês'),
    ('ES-ES', 'Espanhol'),
)


class UserProfile(AbstractUser):
    '''
    Pessoal
    '''

    # Gênero
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True
    )

    '''
    Profissional
    '''

    # Setor da empresa
    sector = models.CharField(
        max_length=50, choices=SECTOR_CHOICES, default=None, null=True,
        blank=True
    )
    # Cargo na empresa
    position = models.CharField(
        max_length=100, choices=POSITION_CHOICES, null=True, blank=True
    )
    # Ramal
    extension = models.CharField(
        blank=True, default=None, max_length=3, null=True
    )
    # Data de admissão na empresa
    admission_date = models.DateField(null=True, blank=True)
    # Turno de trabalho
    period = models.CharField(
        max_length=100, choices=PERIOD_CHOICES, null=True, blank=True
    )

    '''
    Dados de Tickets
    '''

    # Numero total de tickets
    total_tickets = models.IntegerField(
        blank=True, default=None, null=True
    )
    # Numero de tickets em aberto
    open_tickets = models.IntegerField(
        blank=True, default=None, null=True
    )
    # Numero de tickets em andamento
    in_progress_tickets = models.IntegerField(
        blank=True, default=None, null=True
    )
    # Numero de tickets concluídos
    concluded_tickets = models.IntegerField(
        blank=True, default=None, null=True
    )

    '''
    Preferências
    '''

    # Preferência de idioma
    language_preference = models.CharField(
        max_length=50, choices=LANGUAGE_PREFERENCE, default='PT-BR'
    )
    # Preferência de notificação
    notification_preference = models.CharField(
        max_length=20, choices=NOTIFICATION_PREFERENCE_CHOICES, default='SITE'
    )
    # Preferência de tema
    theme_preference = models.CharField(
        max_length=20, choices=THEME_CHOICES, default='LIGHT',
        null=True, blank=True
    )

    '''
    Privacidade
    '''

    # Perfil privado
    public_profile = models.BooleanField(
        max_length=50, default=False
    )

    '''
    Informações de acesso
    '''

    # Sistema operacional
    device_os = models.CharField(
        default=None, max_length=20, null=True, blank=True
    )
    # IPV4 do dispositivo
    device_ip = models.CharField(
        default=None, max_length=30, null=True, blank=True
    )
    # Histórico de IPs (20 últimos)
    device_ip_log = models.TextField(
        default=None, max_length=3000, null=True, blank=True
    )

    def __str__(self):
        # Se last_name for fornecido, pegue apenas o último sobrenome
        last_name = self.last_name.split()[-1] if self.last_name else ""

        # Combina o primeiro nome com o último sobrenome
        full_name = f"{self.first_name} {last_name}"

        return full_name.strip() if full_name.strip() else self.username
