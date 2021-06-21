from django.db import models

from mongoengine import Document, fields
from mongoengine import DynamicDocument

class Course(Document):
    course_id = fields.StringField(required=True)
    course_reviews = fields.StringField()
    course_avg_rating = fields.StringField()
    course_price = fields.StringField()
    course_sample_resource = fields.StringField()
    course_display_picture = fields.StringField()
    course_freq = fields.StringField()
    course_additional_info = fields.StringField()
    course_desc = fields.StringField()
    course_name = fields.StringField()
    course_discount = fields.StringField()
    course_duration = fields.StringField()
    course_exams_covered = fields.StringField()
    course_labels = fields.StringField()
    course_summary = fields.StringField()
    # meta = {'strict': False} #Use this if do not validation of all fields in the document.

