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
from .permissions import IsContributor, IsAuthor, IsProjectAuthorOrContributorReadOnly


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthorOrContributorReadOnly]

    def get_queryset(self):
        if self.action == "list":
            current_user = self.request.user
            projects = [
                contributor.project
                for contributor in Contributor.objects.filter(user_id=current_user.id)
            ]
            return projects
        return Project.objects.all()

    def perform_create(self, serializer: ProjectSerializer):
        project = serializer.save(author=self.request.user)
        contribute = Contributor.objects.create(project=project, user=self.request.user)


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthorOrContributorReadOnly]

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
    permission_classes = [IsAuthenticated, IsContributor, IsAuthor]

    def get_queryset(self):
        project_id = self.kwargs.get("project_pk")
        project_object = get_object_or_404(Project, id=project_id)
        return Issue.objects.filter(project=project_object)

    def perform_create(self, serializer: IssueSerializer):
        project_id = self.kwargs.get("project_pk")
        project_object = get_object_or_404(Project, id=project_id)
        serializer.save(author=self.request.user, project=project_object)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsContributor, IsAuthor]

    def get_queryset(self):
        issue_id = self.kwargs.get("issue_pk")
        issue_object = get_object_or_404(Issue, id=issue_id)
        return Comment.objects.filter(issue=issue_object)

    def perform_create(self, serializer: IssueSerializer):
        issue_id = self.kwargs.get("issue_pk")
        issue_object = get_object_or_404(Issue, id=issue_id)
        serializer.save(user=self.request.user, issue=issue_object)
