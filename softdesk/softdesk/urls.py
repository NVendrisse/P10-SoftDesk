"""
URL configuration for softdesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from software.views import (
    ProjectViewSet,
    ContributorViewSet,
    IssueViewSet,
    CommentViewSet,
)
from authentification.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register("projects", ProjectViewSet, basename="projects")
router.register("users", UserViewSet, basename="users")

project_routers = routers.NestedSimpleRouter(router, r"projects", lookup="project")
project_routers.register(r"contributors", ContributorViewSet, basename="contributors")
project_routers.register(r"issues", IssueViewSet, basename="issues")

issue_routers = routers.NestedSimpleRouter(project_routers, r"issues", lookup="issue")
issue_routers.register(r"comment", CommentViewSet, basename="comments")

# DEBUG URLS
# for url in router.urls:
# print(url)
# for url in project_routers.urls:
# print(url)
# for url in issue_routers.urls:
# print(url)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api/", include(project_routers.urls)),
    path("api/", include(issue_routers.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
