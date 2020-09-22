from django.contrib import admin
from .models import QbankModel, Topic, Question, Choices


# Register your models here.

admin.site.register(QbankModel)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Choices)