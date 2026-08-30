import re

import os
import subprocess
import tempfile
from django.db.models import Count
from openai import OpenAI
from pypdf import PdfReader

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework import generics

from .models import Problem,Submission,Roadmap
from .serializers import ProblemSerializer

@api_view(["POST"])
def run_code(request):

    code = request.data.get("code", "")
    problem_id = request.data.get("problem_id")

    if not code.strip():
        return Response(
            {
                "status": "Error",
                "message": "Code cannot be empty."
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        problem = Problem.objects.get(id=problem_id)
    except Problem.DoesNotExist:
        return Response(
            {
                "status": "Error",
                "message": "Problem not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )

    # Problem ke test cases database se lo
    test_cases = problem.test_cases

    if not test_cases:
        return Response({
            "status": "Error",
            "message": "No test cases available for this problem."
        })

    # Run ke liye first test case use karenge
    test_case = test_cases[0]

    driver_code = test_case.get("driver")
    expected = test_case.get("expected")

    if not driver_code:
        return Response({
            "status": "Error",
            "message": "Invalid test case configuration."
        })

    # Required helper classes
    helper_code = ""

    if problem.topic == "Linked List":

        helper_code = """
class ListNode {

    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
    }
}
"""

    elif problem.topic == "Trees":

        helper_code = """
class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}
"""

    elif problem.title == "Clone Graph":

        helper_code = """
class Node {

    public int val;
    public java.util.List<Node> neighbors;

    public Node() {
        neighbors = new java.util.ArrayList<>();
    }

    public Node(int val) {
        this.val = val;
        neighbors = new java.util.ArrayList<>();
    }
}
"""

    complete_driver = f"""
{helper_code}

public class SolutionRunner {{

    public static void main(String[] args) {{

        {driver_code}

    }}
}}
"""

    try:

        with tempfile.TemporaryDirectory() as temp_dir:

            # User code
            solution_file = os.path.join(
                temp_dir,
                "Solution.java"
            )

            with open(
                solution_file,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(code)

            # Driver
            runner_file = os.path.join(
                temp_dir,
                "SolutionRunner.java"
            )

            with open(
                runner_file,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(complete_driver)

            # Compile
            compile_process = subprocess.run(
                [
                    "javac",
                    solution_file,
                    runner_file
                ],
                capture_output=True,
                text=True,
                timeout=5
            )

            if compile_process.returncode != 0:

                return Response({
                    "status": "Compilation Error",
                    "output": compile_process.stderr
                })

            # Run
            run_process = subprocess.run(
                [
                    "java",
                    "-cp",
                    temp_dir,
                    "SolutionRunner"
                ],
                capture_output=True,
                text=True,
                timeout=3
            )

            if run_process.returncode != 0:

                return Response({
                    "status": "Runtime Error",
                    "output": run_process.stderr
                })

            actual = run_process.stdout.strip()

            return Response({
                "status": "Success",
                "output": actual,
                "expected": expected
            })

    except subprocess.TimeoutExpired:

        return Response({
            "status": "Time Limit Exceeded",
            "output": "Code execution took too long."
        })

    except Exception as e:

        return Response({
            "status": "Error",
            "output": str(e)
        })
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_code(request):
    code = request.data.get("code", "")
    problem_id = request.data.get("problem_id")

    if not code.strip():
        return Response({
            "status": "Error",
            "message": "Code cannot be empty."
        })

    try:
        problem = Problem.objects.get(id=problem_id)
    except Problem.DoesNotExist:
        return Response({
            "status": "Error",
            "message": "Problem not found."
        })

    test_cases = problem.test_cases

    if not test_cases:
        return Response({
            "status": "Error",
            "message": "No test cases available for this problem."
        })

    # Save every submission as Attempted first
    submission = Submission.objects.create(
        user=request.user,
        problem=problem,
        code=code,
        status="Attempted"
    )

    for test_case in test_cases:

        driver_code = test_case.get("driver")
        expected = test_case.get("expected")

        if not driver_code:
            submission.status = "Error"
            submission.save()

            return Response({
                "status": "Error",
                "message": "Invalid test case configuration."
            })

        # Helper classes
        helper_code = ""

        if problem.topic == "Linked List":

            helper_code = """
class ListNode {

    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
    }
}
"""

        elif problem.topic == "Trees":

            helper_code = """
class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}
"""

        elif problem.title == "Clone Graph":

            helper_code = """
class Node {

    public int val;
    public java.util.List<Node> neighbors;

    public Node() {
        neighbors = new java.util.ArrayList<>();
    }

    public Node(int val) {
        this.val = val;
        neighbors = new java.util.ArrayList<>();
    }
}
"""

        complete_driver = f"""
{helper_code}

public class SolutionRunner {{

    public static void main(String[] args) {{

        {driver_code}

    }}
}}
"""

        try:

            with tempfile.TemporaryDirectory() as temp_dir:

                solution_file = os.path.join(
                    temp_dir,
                    "Solution.java"
                )

                runner_file = os.path.join(
                    temp_dir,
                    "SolutionRunner.java"
                )

                with open(
                    solution_file,
                    "w",
                    encoding="utf-8"
                ) as file:
                    file.write(code)

                with open(
                    runner_file,
                    "w",
                    encoding="utf-8"
                ) as file:
                    file.write(complete_driver)

                # Compile
                compile_process = subprocess.run(
                    [
                        "javac",
                        solution_file,
                        runner_file
                    ],
                    capture_output=True,
                    text=True,
                    timeout=5
                )

                if compile_process.returncode != 0:

                    submission.status = "Compilation Error"
                    submission.save()

                    return Response({
                        "status": "Compilation Error",
                        "message": compile_process.stderr
                    })

                # Run
                run_process = subprocess.run(
                    [
                        "java",
                        "-cp",
                        temp_dir,
                        "SolutionRunner"
                    ],
                    capture_output=True,
                    text=True,
                    timeout=3
                )

                if run_process.returncode != 0:

                    submission.status = "Runtime Error"
                    submission.save()

                    return Response({
                        "status": "Runtime Error",
                        "message": run_process.stderr
                    })

                actual = run_process.stdout.strip()

                if actual != expected:

                    submission.status = "Wrong Answer"
                    submission.save()

                    return Response({
                        "status": "Wrong Answer",
                        "message": (
                            f"Expected {expected}, "
                            f"but got {actual}"
                        )
                    })

        except subprocess.TimeoutExpired:

            submission.status = "Time Limit Exceeded"
            submission.save()

            return Response({
                "status": "Time Limit Exceeded",
                "message": "Code execution took too long."
            })

        except Exception as e:

            submission.status = "Error"
            submission.save()

            return Response({
                "status": "Error",
                "message": str(e)
            })

    # Every test case passed
    submission.status = "Accepted"
    submission.save()

    return Response({
        "status": "Accepted",
        "message": "All test cases passed!"
    })

class ProblemListAPIView(generics.ListAPIView):

    queryset = Problem.objects.all().order_by("id")

    serializer_class = ProblemSerializer


class ProblemDetailAPIView(generics.RetrieveAPIView):

    queryset = Problem.objects.all()

    serializer_class = ProblemSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):

    submissions = Submission.objects.filter(
        user=request.user
    )

    # -------------------------
    # Overall Stats
    # -------------------------

    attempted = submissions.values("problem").distinct().count()

    solved = submissions.filter(
        status="Accepted"
    ).values("problem").distinct().count()

    total_submissions = submissions.count()

    accepted_submissions = submissions.filter(
        status="Accepted"
    ).count()

    if total_submissions > 0:
        accuracy = round(
            (accepted_submissions / total_submissions) * 100
        )
    else:
        accuracy = 0

    # -------------------------
    # Topic Stats
    # -------------------------

    topics = []

    all_topics = Problem.objects.values(
        "topic"
    ).distinct()

    for item in all_topics:

        topic = item["topic"]

        attempted_topic = submissions.filter(
            problem__topic=topic
        ).values(
            "problem"
        ).distinct().count()

        solved_topic = submissions.filter(
            problem__topic=topic,
            status="Accepted"
        ).values(
            "problem"
        ).distinct().count()

        total_topic_problems = Problem.objects.filter(
            topic=topic
        ).count()

        if total_topic_problems > 0:
            progress = round(
                (solved_topic / total_topic_problems) * 100
            )
        else:
            progress = 0

        topics.append({
            "topic": topic,
            "attempted": attempted_topic,
            "solved": solved_topic,
            "total": total_topic_problems,
            "progress": progress
        })

    # -------------------------
    # Response
    # -------------------------

    return Response({

        "solved": solved,

        "attempted": attempted,

        "accuracy": accuracy,

        "streak": 0,

        "longest_streak": 0,

        "interview_readiness": min(
            solved * 5,
            100
        ),

        "topics": topics
    })

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def roadmap_api(request):

    # =========================
    # GET → user's saved roadmap
    # =========================

    if request.method == "GET":

        roadmap = Roadmap.objects.filter(
            user=request.user
        ).last()

        if not roadmap:
            return Response({
                "exists": False
            })

        return Response({
            "exists": True,
            "id": roadmap.id,
            "goal": roadmap.goal,
            "level": roadmap.level,
            "problems_per_day": roadmap.problems_per_day,
            "roadmap_data": roadmap.roadmap_data
        })


    # =========================
    # POST → create user's roadmap
    # =========================

    if request.method == "POST":

        goal = request.data.get(
            "goal",
            "Interview Preparation"
        )

        level = request.data.get(
            "level",
            "Beginner"
        )

        problems_per_day = int(
            request.data.get(
                "problems_per_day",
                2
            )
        )


        problems = Problem.objects.all().order_by("id")

        roadmap_data = []


        for problem in problems:

            roadmap_data.append({
                "problem_id": problem.id,
                "title": problem.title,
                "topic": problem.topic,
                "difficulty": problem.difficulty,
                "completed": False
            })


        # Create roadmap for logged-in user

        roadmap = Roadmap.objects.create(
            user=request.user,
            goal=goal,
            level=level,
            problems_per_day=problems_per_day,
            roadmap_data=roadmap_data
        )


        return Response({
            "exists": True,
            "id": roadmap.id,
            "goal": roadmap.goal,
            "level": roadmap.level,
            "problems_per_day": roadmap.problems_per_day,
            "roadmap_data": roadmap.roadmap_data
        })

@api_view(["POST"])
def analyze_resume(request):

    # -----------------------------
    # CHECK FILE
    # -----------------------------

    resume_file = request.FILES.get("resume")

    if not resume_file:
        return Response(
            {
                "status": "Error",
                "message": "Please upload a resume PDF."
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # -----------------------------
    # PDF VALIDATION
    # -----------------------------

    if not resume_file.name.lower().endswith(".pdf"):
        return Response(
            {
                "status": "Error",
                "message": "Only PDF files are supported."
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    if resume_file.size > 5 * 1024 * 1024:
        return Response(
            {
                "status": "Error",
                "message": "Resume must be smaller than 5MB."
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    try:

        # -----------------------------
        # EXTRACT TEXT
        # -----------------------------

        reader = PdfReader(resume_file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        text = text.strip()

        if not text:
            return Response(
                {
                    "status": "Error",
                    "message": "Could not extract text from this PDF."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # lowercase for analysis

        text_lower = text.lower()


        # -----------------------------
        # SKILLS
        # -----------------------------

        skill_keywords = [

            "java",
            "python",
            "javascript",
            "react",
            "django",
            "spring boot",
            "sql",
            "mysql",
            "postgresql",
            "mongodb",
            "html",
            "css",
            "git",
            "github",
            "docker",
            "rest api",
            "machine learning",
            "data structures",
            "algorithms",
            "c++",
            "c",
            "typescript",
            "node.js",
            "express",
            "aws",
            "azure"

        ]


        detected_skills = []

        for skill in skill_keywords:

            if skill in text_lower:
                detected_skills.append(skill)


        # -----------------------------
        # RECOMMENDED SKILLS
        # -----------------------------

        recommended_skills = [

            "git",
            "github",
            "rest api",
            "docker",
            "sql",
            "data structures",
            "algorithms"

        ]

        missing_skills = []

        for skill in recommended_skills:

            if skill not in text_lower:
                missing_skills.append(skill)


        # -----------------------------
        # KEYWORD SCORE
        # -----------------------------

        keyword_score = min(
            round(
                (len(detected_skills) /
                 len(skill_keywords)) * 100
            ),
            100
        )


        # -----------------------------
        # FORMATTING SCORE
        # -----------------------------

        formatting_score = 50

        headings = [
            "education",
            "experience",
            "skills",
            "projects",
            "summary"
        ]

        heading_count = 0

        for heading in headings:

            if heading in text_lower:
                heading_count += 1

        formatting_score += heading_count * 10

        formatting_score = min(
            formatting_score,
            100
        )


        # -----------------------------
        # SKILLS SCORE
        # -----------------------------

        skills_match = min(
            len(detected_skills) * 8,
            100
        )


        # -----------------------------
        # ATS SCORE
        # -----------------------------

        ats_score = round(
            (
                keyword_score * 0.35
                +
                skills_match * 0.35
                +
                formatting_score * 0.30
            )
        )


        # -----------------------------
        # STRENGTHS
        # -----------------------------

        strengths = []

        if len(detected_skills) >= 5:

            strengths.append(
                "Good technical skill coverage."
            )

        if "projects" in text_lower:

            strengths.append(
                "Projects section detected."
            )

        if "education" in text_lower:

            strengths.append(
                "Education section detected."
            )

        if "experience" in text_lower:

            strengths.append(
                "Experience section detected."
            )

        if not strengths:

            strengths.append(
                "Resume content was successfully extracted."
            )


        # -----------------------------
        # IMPROVEMENTS
        # -----------------------------

        improvements = []

        if keyword_score < 50:

            improvements.append(
                "Add more relevant technical keywords."
            )

        if skills_match < 50:

            improvements.append(
                "Add more industry-relevant technical skills."
            )

        if formatting_score < 80:

            improvements.append(
                "Improve resume section structure and formatting."
            )

        if "github" not in text_lower:

            improvements.append(
                "Consider adding your GitHub profile."
            )

        if "linkedin" not in text_lower:

            improvements.append(
                "Consider adding your LinkedIn profile."
            )


        # -----------------------------
        # ATS MESSAGE
        # -----------------------------

        if ats_score >= 80:

            ats_message = (
                "Excellent ATS compatibility. "
                "Your resume is well optimized."
            )

        elif ats_score >= 60:

            ats_message = (
                "Good ATS compatibility, "
                "but there is room for improvement."
            )

        else:

            ats_message = (
                "Your resume needs optimization "
                "to improve ATS compatibility."
            )


        # -----------------------------
        # AI FEEDBACK PLACEHOLDER
        # -----------------------------

        ai_feedback = (
            "Focus on measurable achievements, "
            "relevant keywords, technical skills "
            "and concise project descriptions."
        )


        # -----------------------------
        # RESPONSE
        # -----------------------------

        return Response({

            "status": "Success",

            "ats_score": ats_score,

            "ats_message": ats_message,

            "keyword_match": keyword_score,

            "skills_match": skills_match,

            "formatting_score": formatting_score,

            "skills": detected_skills,

            "missing_skills": missing_skills,

            "strengths": strengths,

            "improvements": improvements,

            "ai_feedback": ai_feedback

        })


    except Exception as e:

        return Response(
            {
                "status": "Error",
                "message": str(e)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
@api_view(["POST"])
def assistant_api(request):

    message = request.data.get("message", "").strip()

    if not message:
        return Response(
            {"message": "Please enter a question."},
            status=400
        )

    try:

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )

        response = client.chat.completions.create(

            model="openrouter/free",

            messages=[
                {
                    "role": "system",
                    "content": """
You are CodePrep AI, a helpful DSA and
software engineering interview coach.

Help the user with:

- DSA concepts
- LeetCode problems
- Java coding
- debugging
- time and space complexity
- interview preparation

Explain concepts clearly and step-by-step.

When explaining code, prefer Java unless
the user specifies another language.

If the user asks for a hint, give a hint
instead of immediately giving the complete solution.
"""
                },

                {
                    "role": "user",
                    "content": message
                }
            ]

        )

        answer = response.choices[0].message.content

        return Response({
            "response": answer
        })

    except Exception as error:

        print("OPENROUTER ERROR:", error)

        return Response(
            {"message": "AI service failed."},
            status=500
        )

@api_view(["POST"])
def mock_interview_api(request):

    action = request.data.get("action")
    topic = request.data.get("topic", "DSA")
    level = request.data.get("level", "Beginner")

    try:

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )


        # =========================
        # START INTERVIEW
        # =========================

        if action == "start":

            prompt = f"""
You are a professional technical interviewer.

Generate ONE {level} level interview question
about {topic}.

The question should be suitable for a software
engineering interview.

Do not provide the answer.

Return only the question.
"""

            response = client.chat.completions.create(

                model="openrouter/free",

                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert technical interviewer."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]

            )

            question = response.choices[0].message.content

            return Response({
                "question": question
            })


        # =========================
        # EVALUATE ANSWER
        # =========================

        if action == "evaluate":

            question = request.data.get("question", "")
            answer = request.data.get("answer", "")

            prompt = f"""
You are evaluating a technical interview answer.

Topic: {topic}
Difficulty: {level}

Question:
{question}

Candidate Answer:
{answer}

Evaluate the candidate.

Give a score from 0 to 20.

Return ONLY valid JSON in this exact format:

{{
    "score": 15,
    "feedback": "Short explanation of the candidate's performance.",
    "correct_approach": "Explain the correct approach."
}}

Do not use markdown.
"""

            response = client.chat.completions.create(

                model="openrouter/free",

                messages=[
                    {
                        "role": "system",
                        "content": "You are a strict but helpful technical interviewer."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]

            )

            content = response.choices[0].message.content

            import json

            result = json.loads(content)

            return Response(result)


        # =========================
        # NEXT QUESTION
        # =========================

        if action == "next":

            previous_question = request.data.get(
                "previous_question",
                ""
            )

            prompt = f"""
Generate ONE new {level} interview question
about {topic}.

Previous question:
{previous_question}

The new question MUST be different from the
previous question.

Return only the question.
"""

            response = client.chat.completions.create(

                model="openrouter/free",

                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert technical interviewer."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]

            )

            question = response.choices[0].message.content

            return Response({
                "question": question
            })


        return Response(
            {"message": "Invalid action."},
            status=400
        )


    except Exception as error:

        print("MOCK INTERVIEW ERROR:", error)

        return Response(
            {"message": "AI service failed."},
            status=500
        )

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def analytics_api(request):

    submissions = Submission.objects.filter(
        user=request.user
    )

    total_submissions = submissions.count()

    accepted = submissions.filter(
        status="Accepted"
    ).count()

    wrong_answers = submissions.filter(
        status="Wrong Answer"
    ).count()

    compilation_errors = submissions.filter(
        status="Compilation Error"
    ).count()

    runtime_errors = submissions.filter(
        status="Runtime Error"
    ).count()

    attempted_problems = submissions.values(
        "problem"
    ).distinct().count()

    solved_problems = submissions.filter(
        status="Accepted"
    ).values(
        "problem"
    ).distinct().count()

    total_problems = Problem.objects.count()

    accuracy = 0

    if total_submissions > 0:
        accuracy = round(
            (accepted / total_submissions) * 100
        )

    # Difficulty stats

    difficulty_stats = []

    for difficulty in ["Easy", "Medium", "Hard"]:

        total = Problem.objects.filter(
            difficulty=difficulty
        ).count()

        solved = submissions.filter(
            problem__difficulty=difficulty,
            status="Accepted"
        ).values(
            "problem"
        ).distinct().count()

        difficulty_stats.append({
            "difficulty": difficulty,
            "solved": solved,
            "total": total
        })

    # Topic stats

    topic_stats = []

    topics = Problem.objects.values(
        "topic"
    ).distinct()

    for item in topics:

        topic = item["topic"]

        total = Problem.objects.filter(
            topic=topic
        ).count()

        solved = submissions.filter(
            problem__topic=topic,
            status="Accepted"
        ).values(
            "problem"
        ).distinct().count()

        topic_stats.append({
            "topic": topic,
            "solved": solved,
            "total": total
        })

    # Recent submissions

    recent_submissions = []

    for submission in submissions.select_related(
        "problem"
    ).order_by("-created_at")[:10]:

        recent_submissions.append({
            "problem": submission.problem.title,
            "status": submission.status,
            "difficulty": submission.problem.difficulty,
            "topic": submission.problem.topic,
            "created_at": submission.created_at
        })

    return Response({

        "total_problems": total_problems,

        "solved_problems": solved_problems,

        "attempted_problems": attempted_problems,

        "total_submissions": total_submissions,

        "accepted": accepted,

        "wrong_answers": wrong_answers,

        "compilation_errors": compilation_errors,

        "runtime_errors": runtime_errors,

        "accuracy": accuracy,

        "difficulty_stats": difficulty_stats,

        "topic_stats": topic_stats,

        "recent_submissions": recent_submissions
    })

@api_view(["POST"])
@permission_classes([AllowAny])
def signup_api(request):

    username = request.data.get("username", "").strip()
    email = request.data.get("email", "").strip()
    password = request.data.get("password", "")

    if not username or not email or not password:
        return Response(
            {"message": "All fields are required."},
            status=400
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"message": "Username already exists."},
            status=400
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {"message": "Email already exists."},
            status=400
        )

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return Response(
        {
            "message": "Account created successfully."
        },
        status=201
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def login_api(request):

    username = request.data.get("username", "").strip()
    password = request.data.get("password", "")

    if not username or not password:
        return Response(
            {"message": "Username and password are required."},
            status=400
        )

    user = authenticate(
        username=username,
        password=password
    )

    if user is None:
        return Response(
            {"message": "Invalid username or password."},
            status=401
        )

    refresh = RefreshToken.for_user(user)

    return Response({
        "message": "Login successful.",
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    })