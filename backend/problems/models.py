from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):

    DIFFICULTY_CHOICES = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True
    )

    description = models.TextField()

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES
    )

    topic = models.CharField(
        max_length=100
    )

    acceptance = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )

    examples = models.JSONField(
        default=list
    )

    constraints = models.JSONField(
        default=list
    )
    test_cases = models.JSONField(
    default=list
)

    starter_code = models.TextField()

    expected_time = models.CharField(
        max_length=50,
        blank=True
    )

    expected_space = models.CharField(
        max_length=50,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

class Roadmap(models.Model):

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="roadmaps",
    null=True,
    blank=True
)

    goal = models.CharField(max_length=100)

    level = models.CharField(max_length=50)

    problems_per_day = models.IntegerField(default=2)

    roadmap_data = models.JSONField(default=list)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.goal}"

class Submission(models.Model):

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="submissions",
    null=True,
    blank=True
)
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    code = models.TextField()

    status = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.status}"