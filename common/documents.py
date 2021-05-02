from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from courses.models import Course
from institutes.models import Institute
from .models import Exam

courses = Index('courses')

@registry.register_document
@courses.document
class CourseDocument(Document):
    class Django:
        model = Course

        fields = [
            'course_name',
            'course_desc',
            'course_summary',
        ]
