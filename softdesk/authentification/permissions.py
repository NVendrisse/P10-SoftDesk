from rest_framework import permissions


class IsAdminOrIsSelf(permissions.BasePermission):
    """
    Permission for the users management
    """

    def has_permission(self, request, view):
        print(view.action)
        self.message = "Permission denied, you are not an administrator"
        if view.action == "list":
            return bool(request.user.is_superuser)
        return True

    def has_object_permission(self, request, view, obj):
        print(view.action)
        self.message = "Permission denied, you can't delete, modify or get some other user informations"
        if view.action == "destroy":
            self.message = "Permission denied, you can't delete a user, you are not an administrator"
            return bool(request.user.is_superuser)
        return bool(request.user == obj)
