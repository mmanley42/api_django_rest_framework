from rest_framework import serializers
from .models import Posts, Likes
import re
# What will show between the different views

# Serializer for the likes That shows which post it likes
class LikesSerializer(serializers.ModelSerializer):
	posted = serializers.SerializerMethodField()
	class Meta:
		model = Likes
		fields = [
			'post_key',
			'posted',
			'like',
			'id',
		]
	def get_posted(self, obj):
		if Posts.objects.all() is not None:
			return obj.post_key.post_text
		return None

# A Serializer for the main page
class PostSerializer(serializers.ModelSerializer):
	like_count = serializers.SerializerMethodField()
	class Meta:
		model = Posts
		fields = [
			'post_text',
			'like_count',
			'id',
		]
	# Function to count the number of likes for the instance object
	def get_like_count(self, obj):
		if Likes.objects.all() is not None:
			return Likes.objects.filter(post_key=obj.pk, like=True).count()
		return 0

# A Serializer to show on the Detail page of the posts
class PostDetailSerializer(serializers.ModelSerializer):
	like_count = serializers.SerializerMethodField()
	class Meta:
		model = Posts
		fields = [
			'username',
			'post_text',
			'pub_date',
			'last_update',
			'like_count',
			'id',
		]
	def get_like_count(self, obj):
		print (Likes.post_key)
		if Likes.objects.all() is not None:
			return Likes.objects.filter(post_key=obj.pk, like=True).count()
		return 0
