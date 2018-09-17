from .models import Posts, Likes
from .serializers import PostSerializer, PostDetailSerializer, LikesSerializer
from django.utils import timezone
from rest_framework import generics
from django.shortcuts import redirect

# Create your views here.

def redirect_url(request):
	response = redirect('/posts/')
	return response

# GET command
class ListView(generics.ListAPIView):
	queryset = Posts.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]
	serializer_class = PostSerializer

# POST command
class CreatePostView(generics.CreateAPIView):
	queryset = Posts.objects.all()
	serializer_class = PostDetailSerializer

# GET by <id>, PUT & DELETE
class DetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Posts.objects.filter(pub_date__lte=timezone.now())
	serializer_class = PostDetailSerializer

# POST for the Likes feature
class CreateLikeView(generics.CreateAPIView):
	queryset = Posts.objects.filter(pub_date__lte=timezone.now())
	serializer_class = LikesSerializer

# GET by <id>, PUT & DELETE for the Likes feature
class ResetLikesView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Likes.objects.all()
	serializer_class = LikesSerializer
# GET the list and pks for the likes objects
class LikeIndexView(generics.ListAPIView):
	queryset = Likes.objects.all()
	serializer_class = LikesSerializer
