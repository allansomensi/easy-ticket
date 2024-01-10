from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import UserProfile


class UserAdmin(UserAdmin):

    list_display = ('username', 'email', 'sector', 'extension', 'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Informações Pessoais', {
                'fields': (
                    'first_name', 'last_name', 'gender', 'email',
                )
            }
        ),
        (
            'Informações Profissionais', {
                'fields': (
                    'sector',  'position', 'extension', 'admission_date',
                    'period',
                )
            }
        ),
        (
            'Dados de Tickets', {
                'fields': (
                    'total_tickets',  'open_tickets', 'in_progress_tickets',
                    'concluded_tickets',
                )
            }
        ),
        (
            'Preferências', {
                'fields': (
                    'language_preference',  'notification_preference',
                    'theme_preference',
                )
            }
        ),
        (
            'Privacidade', {
                'fields': (
                    'public_profile',
                )
            }
        ),
        (
            'Informações de acesso', {
                'fields': (
                    'device_os', 'device_ip', 'device_ip_log',
                )
            }
        ),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff',
                    'is_superuser', 'groups', 'user_permissions',
                )
            }
        ),
        ('Datas Importantes', {'fields': ('date_joined', 'last_login')}),
    )


admin.site.register(UserProfile, UserAdmin)
