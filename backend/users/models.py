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

THEME_CHOICES = (
    ('LIGHT', 'Modo Claro'),
    ('DARK', 'Modo Escuro'),
)


class UserProfile(AbstractUser):
    sector = models.CharField(
        max_length=50, choices=SECTOR_CHOICES, default=None, null=True, blank=True)  # noqa: E501
    extension = models.CharField(
        blank=True, default=None, max_length=3, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    position = models.CharField(
        max_length=100, choices=POSITION_CHOICES, null=True, blank=True)
    period = models.CharField(
        max_length=100, choices=PERIOD_CHOICES, null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    theme_preference = models.CharField(
        max_length=20, choices=THEME_CHOICES, default='LIGHT', null=True, blank=True)  # noqa: E501

    def get_sector_display(self):
        return dict(SECTOR_CHOICES).get(self.sector, self.sector)

    def get_gender_display(self):
        return dict(GENDER_CHOICES).get(self.gender, self.gender)

    def get_position_display(self):
        return dict(POSITION_CHOICES).get(self.position, self.position)

    def get_period_display(self):
        return dict(PERIOD_CHOICES).get(self.period, self.period)

    def save(self, *args, **kwargs):
        # Defina um tema padrão se não houver preferência definida
        if not self.theme_preference:
            self.theme_preference = 'LIGHT'
        super().save(*args, **kwargs)

    def __str__(self):
        # Se last_name for fornecido, pegue apenas o último sobrenome
        last_name = self.last_name.split()[-1] if self.last_name else ""

        # Combine o primeiro nome com o último sobrenome
        full_name = f"{self.first_name} {last_name}"

        return full_name.strip() if full_name.strip() else self.username
