from rest_framework import permissions
from .models import Contributor, Project
from django.shortcuts import get_object_or_404


class IsProjectAuthorOrContributorReadOnly(permissions.BasePermission):
    """
    Permission for the project author for project and contributor management
    """

    message = (
        "Permission denied, you are not the author, or a contributor of this project"
    )

    def has_object_permission(self, request, view, obj):

        if view.action == "retrieve":
            contributors = [
                contrib.user for contrib in Contributor.objects.filter(project=obj)
            ]
            return bool(request.user in contributors)

        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            return bool(obj.author == request.user)
        except AttributeError:
            return bool(obj.project.author == request.user)


class CanAddContributor(permissions.BasePermission):
    """
    Permission in order to add a new contributor to a project,
    must be the project author
    """

    message = "You can't add a contributor to this project, please contact the author"

    def has_permission(self, request, view):
        project_id = view.kwargs.get("project_pk")
        project_object = get_object_or_404(Project, id=project_id)
        return bool(project_object.author == request.user)


class IsAuthor(permissions.BasePermission):
    """
    Permission for the author, work with project, issue and comment
    """

    message = "Permission denied, you are not the author of this project"

    def has_object_permission(self, request, view, obj):
        return bool(obj.author == request.user)


class IsContributor(permissions.BasePermission):
    """
    Permission for the contributors
    """

    message = "Permission denied, you are not a contributor of this project"

    def has_permission(self, request, view):
        project_id = view.kwargs.get("project_pk")
        project_object = get_object_or_404(Project, id=project_id)
        contributors = [
            contributor.user
            for contributor in Contributor.objects.filter(project=project_object)
        ]

        return bool(request.user in contributors)
