from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
	)
	title = models.CharField(max_length=250)	#field for the post title
	slug = models.SlugField(max_length=250, unique_for_date='publish') #used for URLs to make them seo friendly
	author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.DO_NOTHING,)
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now) #used for publication date
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	class Meta:
		ordering = ('-publish',) #here we're sorting results by the publish
								 #field in (-) decending order

	def __str__(self):
		return self.title
