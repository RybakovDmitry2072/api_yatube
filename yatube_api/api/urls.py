from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentsViewSet

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)


comment_list = CommentsViewSet.as_view({
    'post': 'create',
    'get': 'list',

})

comment_detail = CommentsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('posts/<int:post_id>/comments/', comment_list),
    path('posts/<int:post_id>', comment_list),
    path('posts/<int:post_id>/comments/<comment_id>/', comment_detail),
    path('', include(router.urls)),
]
