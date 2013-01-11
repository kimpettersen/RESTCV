from rest_framework import serializers
from api.education.models import Education


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = ('university', 'city', 'country', 'start_date', 'end_date', 'title', 'description',)
