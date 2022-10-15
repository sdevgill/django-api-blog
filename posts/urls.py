from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, PostViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("", PostViewSet, basename="post")

urlpatterns = router.urls

# urlpatterns = [
#     path("users/", UserList.as_view()),
#     path("users/<int:pk>/", UserDetail.as_view()),
#     path("", PostList.as_view(), name="post_list"),
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
# ]
