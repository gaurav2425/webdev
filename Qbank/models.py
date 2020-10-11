from django.db import models
from django.contrib.auth.models import User



class QbankModel(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    QbankModel = models.ForeignKey(QbankModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.subject

class Subtopic(models.Model):
    subtopicname = models.CharField(max_length=255)
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.subtopicname



class Question(models.Model):
    id = models.CharField(max_length=64, unique=True, primary_key=True)
    question_stem = models.TextField(max_length=4000)
    Topic = models.ForeignKey(Topic, related_name='topic', default='UniqueCode', on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Choices(models.Model):
    id = models.CharField(max_length=64, unique=True, primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.choice_text
