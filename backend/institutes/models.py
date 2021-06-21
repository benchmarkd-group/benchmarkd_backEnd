from django.db import models

from mongoengine import Document, fields
from mongoengine import DynamicDocument

class Institute(Document):
    insti_id = fields.StringField(required=True)
    insti_name = fields.StringField()
    insti_avg_rating = fields.StringField()
    insti_display_picture = fields.StringField()
    insti_branches = fields.ListField()
    insti_desc = fields.StringField()
    insti_emails = fields.ListField()
    insti_past_achievements = fields.ListField()
    insti_exams_covered = fields.ListField()
    insti_labels = fields.ListField()
    insti_summary = fields.StringField()
    insti_courses = fields.ListField()

