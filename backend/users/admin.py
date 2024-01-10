from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import UserProfile


class UserAdmin(UserAdmin):

    list_display = ('username', 'email', 'sector', 'extension',  'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {
         'fields': ('first_name', 'last_name', 'gender', 'email', 'theme_preference')}),
        ('Informações Profissionais', {
         'fields': ('sector',  'extension', 'position', 'period', 'admission_date')}),
        ('Permissões', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('date_joined', 'last_login')}),
    )


admin.site.register(UserProfile, UserAdmin)
