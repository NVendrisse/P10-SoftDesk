from rest_framework.serializers import ModelSerializer
from software.models import Project, Contributor, Comment, Issue


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "author", "name", "description", "type"]
        read_only_fields = ["author"]


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "user", "project"]
        read_only_fields = ["project"]


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "author",
            "project",
            "title",
            "description",
            "attributed_user",
            "nature",
            "priority",
            "status",
        ]
        read_only_fields = ["author", "project"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "text"]
        read_only_fields = ["author", "issue"]
