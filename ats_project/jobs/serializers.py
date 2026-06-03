from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:

        model = Job

        fields = '__all__'


class PublicJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "description",
            "pay_start",
            "pay_end",
            "location",
            "job_type",
            "location_type",
            "slug",
        ]