from rest_framework.permissions import SAFE_METHODS, BasePermission


class BanPermission(BasePermission):
    """Базовый класс разрешений с проверкой - забанен ли пользователь."""

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_active
        )


class OwnerUserOrReadOnly(BanPermission):
    """
    Разрешение на создание и изменение только для админа и пользователя.
    Остальным только чтение объекта.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_active
            and request.user == obj.author
            or request.user.is_staff
        )
