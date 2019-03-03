from django.db import models
from django.utils import timezone 
# from django.urls import 


from django.contrib.auth import get_user_model
User = get_user_model()

import misaka

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	detail = models.TextField(default="")
	detail_html = models.TextField(default="")
	created_date = models.DateTimeField(default=timezone.now)
	pub_date = models.DateTimeField(null=True, blank=True)


	def save(self, *args, **kwargs):
		self.detail_html = misaka.html(self.detail)
		super().save(args, kwargs)

	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"

	def __str__(self):
		return self.title


class Comment(models.Model):
	writer = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField(default="")
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	com_date = models.DateTimeField(default=timezone.now)
	approve = models.BooleanField(default=False)

	def approved(self):
		self.approve = True
		self.save()

	class Meta:
		verbose_name = "Comment"
		verbose_name_plural = "Comments"

	def __str__(self):
		return self.comment
