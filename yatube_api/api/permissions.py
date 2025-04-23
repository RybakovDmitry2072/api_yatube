from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Всегда разрешаем безопасные методы (GET, HEAD, OPTIONS)
        # но только для аутентифицированных пользователей
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        
        # Для изменений также требуем аутентификацию
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Разрешаем только аутентифицированным пользователям
        if not request.user.is_authenticated:
            return False
            
        # Разрешаем безопасные методы для всех аутентифицированных
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Для изменений проверяем, что пользователь - автор
        return obj.author == request.user