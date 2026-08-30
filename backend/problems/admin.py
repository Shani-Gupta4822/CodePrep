from django.contrib import admin

from .models import Problem


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "difficulty",
        "topic",
        "acceptance",
    )

    list_filter = (
        "difficulty",
        "topic",
    )

    search_fields = (
        "title",
        "description",
        "topic",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }