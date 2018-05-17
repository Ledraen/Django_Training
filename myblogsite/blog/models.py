from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
	def get_queryset(self):  # returns the queryset
		return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
	STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
	)
	title = models.CharField(max_length=250)	# field for the post title
	slug = models.SlugField(max_length=250, unique_for_date='publish') # used for URLs to make them seo friendly
	author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.DO_NOTHING,)
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now) # used for publication date
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	objects = models.Manager()	# this is the default manager
	published = PublishedManager	# this is the Dahl specific manager

	class Meta:
		ordering = ('-publish',) # here we're sorting results by the publish
								 # field in (-) decending order

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.publish.year,
											     self.publish.strftime('%m'),
												 self.publish.strftime('%d'),
												 self.slug])
	#nb: the strftime fn builds url month and day using leading zeros											 self.slug])
