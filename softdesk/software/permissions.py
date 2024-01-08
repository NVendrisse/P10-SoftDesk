from rest_framework import permissions


class IsContributor(permissions.BasePermission):
    edit_method = ("GET", "POST", "PATCH", "DEL")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if obj.user == request.user:
            return True

        return False
