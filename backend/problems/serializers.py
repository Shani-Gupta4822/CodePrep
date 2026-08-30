from rest_framework import serializers

from .models import Problem


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem

        fields = [
    "id",
    "title",
    "slug",
    "description",
    "difficulty",
    "topic",
    "acceptance",
    "examples",
    "constraints",
    "test_cases",
    "starter_code",
    "expected_time",
    "expected_space",
    "created_at",
    "updated_at",
]