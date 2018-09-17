from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime

# Create your models here.

def time_stamps(date):
	if date < timezone.now():
		raise ValidationError("Please write a valid date")

class Posts(models.Model):
	username = models.CharField(max_length=20)
	post_text = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(timezone.now(), validators=[time_stamps])

	# to make sure it won't be published before the timestamp is th actual date
	def was_published_at(self):
		now = timezone.now()
		return self.last_update <= now

class Likes(models.Model):
	post_key = models.ForeignKey(Posts, on_delete=models.CASCADE)
	like = models.NullBooleanField()
