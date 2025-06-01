from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import PostViewSet, UserViewSet

router = DefaultRouter()
router.register('post', PostViewSet, basename='Post')
router.register('user', UserViewSet, basename='User')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]