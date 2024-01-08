from rest_framework.viewsets import ModelViewSet
from software.models import Project, Contributor, Comment, Issue
from software.serializer import (
    ProjectSerializer,
    ContributorSerializer,
    CommentSerializer,
    IssueSerializer,
)
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .permissions import IsContributor


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer: ProjectSerializer):
        project = serializer.save(author=self.request.user)


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get("project_pk")
        project_object = get_object_or_404(Project, id=project_id)
        return Contributor.objects.filter(project=project_object)

    def perform_create(self, serializer: ContributorSerializer):
        project_id = self.kwargs.get("project_pk")
        project_object = get_object_or_404(Project, id=project_id)
        serializer.save(project=project_object)


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsContributor]

    def get_queryset(self):
        project_id = self.kwargs.get("project_pk")
        project_object = get_object_or_404(Project, id=project_id)
        return Issue.objects.filter(project=project_object)

    def perform_create(self, serializer: IssueSerializer):
        project_id = self.kwargs.get("project_pk")
        project_object = get_object_or_404(Project, id=project_id)
        serializer.save(user=self.request.user, project=project_object)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
