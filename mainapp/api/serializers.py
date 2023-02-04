from idlelib.searchengine import search_reverse

from mainapp.models import School,Student
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class SchoolSerializer(ModelSerializer):
    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('Name must be 4 character')
        return value

    class Meta:
        model = School
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('Name must be 4 character')
        return value

    class Meta:
        model = Student
        fields = '__all__'