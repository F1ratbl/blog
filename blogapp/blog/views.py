from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, generics

# Create your views here.
from .models import Post, User
from .serializers import PostSerializer, UserSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WeatherViews(generics.GenericAPIView, generics.CreateAPIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'weather.html')