from rest_framework.response import Response
from rest_framework.views import APIView
from models import Project, Contributor, Comment, Issue
from serializer import (
    ProjectSerializer,
    ContributorSerializer,
    CommentSerializer,
    IssueSerializer,
)


class ProjectView(APIView):
    def get(self, *arg, **kwarg):
        projects = Project.objects.all()
        serialized = ProjectSerializer(projects, many=True)
        return Response(serialized.data)


class ContributorView(APIView):
    def get(self, *arg, **kwarg):
        contributors = Contributor.objects.all()
        serialized = ContributorSerializer(contributors, many=True)
        return Response(serialized.data)


class IssueView(APIView):
    def get(self, *arg, **kwarg):
        issues = Issue.objects.all()
        serialized = IssueSerializer(issues, many=True)
        return Response(serialized.data)


class CommentView(APIView):
    def get(self, *arg, **kwarg):
        comments = Comment.objects.all()
        serialized = CommentSerializer(comments, many=True)
        return Response(serialized.data)
