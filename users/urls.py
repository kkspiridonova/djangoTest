from django.urls import path
from .views import login_user, registration_user, logout_user
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

urlpatterns = [
    path('login', login_user, name='login'),
    path('register', registration_user, name='register'),
    path('logout', logout_user, name='logout'),
]

def check_permissions(request):
    """Проверка прав и статуса пользователя"""
    
    output = [
        f'Активен: {request.user.is_active}',
        f'Анонимный: {request.user.is_anonymous}',
        f'Аутентифицирован: {request.user.is_authenticated}',
        f'Персонал: {request.user.is_staff}',
        f'Суперпользователь: {request.user.is_superuser}',
        f'Может добавлять товары: {request.user.has_perm("shop.add_product")}',
        f'Может изменять товары: {request.user.has_perm("shop.change_product")}',
    ]
    return HttpResponse("<br>".join(output))