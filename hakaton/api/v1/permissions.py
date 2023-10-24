from rest_framework import permissions


class IsOwnerPut(permissions.BasePermission):
    """
    Предоставляет доступ на обновление (PUT) личных данных только автору.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj
