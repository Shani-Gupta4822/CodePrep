from django.urls import path

from .views import (
    run_code,
    submit_code,
    dashboard_stats,
    ProblemListAPIView,
    ProblemDetailAPIView,
    roadmap_api,
    analyze_resume,
    assistant_api,
    mock_interview_api,
    analytics_api,
    signup_api,
    login_api
)


urlpatterns = [

    path(
        "",
        ProblemListAPIView.as_view(),
        name="problem-list",
    ),

    path(
        "run/",
        run_code,
        name="run-code",
    ),
    path(
    "submit/",
    submit_code,
    name="submit-code",
),

    path(
        "<int:pk>/",
        ProblemDetailAPIView.as_view(),
        name="problem-detail",
    ),
    path(
    "dashboard-stats/",
    dashboard_stats,
),
path("roadmap/", roadmap_api),
path(
    "resume/analyze/",
    analyze_resume,
    name="analyze-resume"
),

path(
    "assistant/",
    assistant_api,
    name="assistant-api"
),
path(
    "mock-interview/",
    mock_interview_api,
    name="mock-interview"
),

path(
    "analytics/",
    analytics_api,
    name="analytics"
),

path(
    "auth/signup/",
    signup_api,
    name="signup",
),

path(
    "auth/login/",
    login_api,
    name="login",
),
]