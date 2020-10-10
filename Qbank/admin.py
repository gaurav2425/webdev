from django.contrib import admin
from .models import QbankModel, Topic, Subtopic, Question, Choices


# Register your models here.

admin.site.register(QbankModel)
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(Question)
admin.site.register(Choices)