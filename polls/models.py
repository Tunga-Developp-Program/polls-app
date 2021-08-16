from django.db import models

# Create your models here.
from django.db import models

# Question model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True)
    def __str__(self):
        return f'{self.question_text}'

# Choice Model
class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices' ,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.choice_text}'
