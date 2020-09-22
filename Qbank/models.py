from django.db import models
from django.contrib.auth.models import User



class QbankModel(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    QbankModel = models.ForeignKey(QbankModel, related_name='topics', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.subject



class Question(models.Model):
    id = models.CharField(max_length=64, unique=True, primary_key=True)
    question_stem = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    Topic = models.ForeignKey(Topic, related_name='topic', default='UniqueCode', on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Choices(models.Model):
    id = models.CharField(max_length=64, unique=True, primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.choice_text
