from rest_framework import permissions
from .models import Contributor, Project
from django.shortcuts import get_object_or_404


class IsProjectAuthorOrContributorReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        project_id = view.kwargs.get("pk")
        # obj
        if view.action == "retrieve":
            contributors = [
                contrib.user
                for contrib in Contributor.objects.filter(project=project_id)
            ]
            return bool(request.user in contributors)

        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            return bool(obj.author == request.user)
        except AttributeError:
            return bool(obj.project.author == request.user)


# CanAddContributor has_permission


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.author == request.user)


class IsContributor(permissions.BasePermission):
    message = "You are not a contributor of this project"

    def has_permission(self, request, view):
        project_id = view.kwargs.get("pk")
        project_object = get_object_or_404(Project, id=project_id)
        contributors = [
            contributor.user
            for contributor in Contributor.objects.filter(project=project_object)
        ]
        print(contributors)
        return bool(request.user in contributors)
