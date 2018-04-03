from django.db import models

# Create your models here.

# Creates two models: Question (containing a question and date)
# and Choice containing the text of choice and a vote tally.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date Published')


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)