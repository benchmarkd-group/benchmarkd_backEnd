from django.db import models

from mongoengine import Document, fields
from mongoengine import DynamicDocument

class Exam(Document):
    exam_id = fields.StringField(required=True)
    exam_name = fields.StringField()
    exam_desc = fields.StringField()
    exam_summary = fields.StringField()
    institutes_list= fields.ListField()
    courses_list= fields.ListField()


