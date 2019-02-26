import uuid
from django.db import models

QUESTION_TYPES = (
    (1, 'Multiple choices'),
    (2, 'Text field'),
    (3, 'Char field'),
    (4, 'File upload'),
)

class EstimateRequest(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=20)

    read = models.BooleanField(default=False)
    replied = models.BooleanField(default=False)

class Question(models.Model):
    title = models.CharField(max_length=600)
    description = models.TextField()
    question_type = models.IntegerField(choices=QUESTION_TYPES)

class QuestionChoice(models.Model):
    name = models.CharField(max_length=300)