from rest_framework.serializers import ModelSerializer

from models import Project, Contributor, Comment, Issue


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name"]


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "user", "project"]


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ["id", "project", "status"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "project", "text"]
