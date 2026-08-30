import {
  Activity,
  ArrowRight,
  BarChart3,
  Bot,
  CalendarDays,
  CheckCircle2,
  Flame,
  Route,
  ShieldCheck,
  Sparkles,
  Target,
  Trophy
} from "lucide-react";

import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

import "./Dashboard.css";


function StatCard({ icon, title, value, subtitle }) {

  return (
    <div className="stat-card">

      <div className="stat-icon">
        {icon}
      </div>

      <div className="stat-content">

        <span className="stat-title">
          {title}
        </span>

        <strong className="stat-value">
          {value}
        </strong>

        <span className="stat-subtitle">
          {subtitle}
        </span>

      </div>

    </div>
  );
}


function Dashboard() {

  const navigate = useNavigate();


  const [stats, setStats] = useState({
    solved: 0,
    attempted: 0,
    accuracy: 0,
    streak: 0,
    longest_streak: 0,
    interview_readiness: 0,
    topics: []
  });


  const [dailyProblem, setDailyProblem] = useState(null);


  const user = JSON.parse(
    localStorage.getItem("user") || "{}"
  );


  useEffect(() => {

    const fetchStats = async () => {

      const token = localStorage.getItem("access");

      if (!token) {
        navigate("/login");
        return;
      }


      try {

        const response = await fetch(
          "http://127.0.0.1:8000/api/problems/dashboard-stats/",
          {
            method: "GET",

            headers: {
              "Authorization": `Bearer ${token}`,
            },
          }
        );


        const data = await response.json();


        if (response.status === 401) {

          localStorage.removeItem("access");
          localStorage.removeItem("refresh");
          localStorage.removeItem("user");

          navigate("/login");

          return;
        }


        if (!response.ok) {
          throw new Error(
            data.message || "Failed to load dashboard stats"
          );
        }


        console.log(
          "DASHBOARD STATS:",
          data
        );

        setStats(data);


      } catch (error) {

        console.error(
          "Dashboard stats error:",
          error
        );

      }

    };


    fetchStats();

  }, [navigate]);


  useEffect(() => {

    fetch(
      "http://127.0.0.1:8000/api/problems/"
    )
      .then((response) => response.json())
      .then((data) => {

        console.log(
          "PROBLEMS FOR DAILY:",
          data
        );


        if (data.length > 0) {

          const today = new Date();

          const start = new Date(
            today.getFullYear(),
            0,
            0
          );


          const diff =
            today -
            start +
            (
              (
                start.getTimezoneOffset() -
                today.getTimezoneOffset()
              ) *
              60 *
              1000
            );


          const oneDay =
            1000 * 60 * 60 * 24;


          const dayOfYear =
            Math.floor(
              diff / oneDay
            );


          const index =
            dayOfYear % data.length;


          setDailyProblem(
            data[index]
          );

        }

      })
      .catch((error) => {

        console.error(
          "Daily problem error:",
          error
        );

      });

  }, []);


  return (

    <div className="dashboard">


      {/* =========================
          HEADER
      ========================== */}

      <div className="dashboard-header">

        <div>

          <span className="dashboard-eyebrow">
            YOUR WORKSPACE
          </span>


          <h1>
            Welcome back,{" "}
            {user.username || "Shani"} 👋
          </h1>


          <p>
            Build consistency. Crack interviews.
            One problem at a time.
          </p>

        </div>

      </div>


      {/* =========================
          PROBLEM OF THE DAY
      ========================== */}

      <section className="problem-day">

        <div className="problem-day-left">

          <div className="problem-label">

            <CalendarDays size={14} />

            PROBLEM OF THE DAY

            <span>
              {new Date().toLocaleDateString(
                "en-IN",
                {
                  weekday: "short",
                  day: "2-digit",
                  month: "short"
                }
              )}
            </span>

          </div>


          <h2>
            {dailyProblem
              ? dailyProblem.title
              : "Loading..."}
          </h2>


          <p>
            {dailyProblem
              ? dailyProblem.description
              : "Loading today's problem..."}
          </p>


          {dailyProblem && (

            <div className="problem-tags">

              <span
                className={`tag ${
                  dailyProblem.difficulty === "Easy"
                    ? "easy"
                    : ""
                }`}
              >
                {dailyProblem.difficulty}
              </span>


              <span className="tag">
                {dailyProblem.topic}
              </span>

            </div>

          )}


          <button
            className="primary-btn"
            onClick={() => {

              if (dailyProblem) {

                navigate(
                  `/problems/${dailyProblem.id}`
                );

              }

            }}
          >

            Solve now

            <ArrowRight size={15} />

          </button>

        </div>


        <div className="problem-day-right">

          <div className="binary-visual">

            <div className="binary-box active">
              1
            </div>

            <div className="binary-box">
              3
            </div>

            <div className="binary-box">
              5
            </div>

            <div className="binary-box target">
              7
            </div>

            <div className="binary-box">
              9
            </div>

          </div>


          <span>
            {dailyProblem?.expected_time || "O(n)"}
          </span>

        </div>

      </section>


      {/* =========================
          STATISTICS
      ========================== */}

      <div className="stats-grid">

        <StatCard
          icon={<CheckCircle2 size={17} />}
          title="Solved"
          value={stats.solved}
          subtitle="Start solving"
        />


        <StatCard
          icon={<Activity size={17} />}
          title="Attempted"
          value={stats.attempted}
          subtitle="No attempts yet"
        />


        <StatCard
          icon={<Target size={17} />}
          title="Accuracy"
          value={`${stats.accuracy}%`}
          subtitle="Solve to unlock"
        />


        <StatCard
          icon={<Flame size={17} />}
          title="Current Streak"
          value={`${stats.streak}d`}
          subtitle={`Longest: ${stats.longest_streak}d`}
        />


        <StatCard
          icon={<ShieldCheck size={17} />}
          title="Interview Readiness"
          value={`${stats.interview_readiness}%`}
          subtitle="20 solves to unlock"
        />

      </div>


      {/* =========================
          LOWER GRID
      ========================== */}

      <div className="dashboard-grid">


        {/* ROADMAP */}

        <section className="dashboard-card">

          <div className="card-header">

            <div className="card-title">

              <Route size={16} />

              Your Roadmap

            </div>


            <button
              className="card-link"
              onClick={() =>
                navigate("/roadmap")
              }
            >
              View roadmap
            </button>

          </div>


          <div className="roadmap-content">

            <div className="roadmap-icon">

              <Route size={22} />

            </div>


            <div>

              <h3>
                No roadmap yet
              </h3>

              <p>
                Generate a personalized DSA study
                plan based on your goals.
              </p>


              <button
                className="text-button"
                onClick={() =>
                  navigate("/roadmap")
                }
              >

                Generate your first roadmap

                <ArrowRight size={13} />

              </button>

            </div>

          </div>

        </section>


        {/* TOPICS */}

        <section className="dashboard-card">

          <div className="card-header">

            <div className="card-title">

              <BarChart3 size={16} />

              Topics

            </div>


            <button
              className="card-link"
              onClick={() =>
                navigate("/Problems")
              }
            >
              Explore
            </button>

          </div>


          <div className="topics-list">

            {stats.topics &&
            stats.topics.length > 0 ? (

              stats.topics
                .slice(0, 5)
                .map((topic) => (

                  <div
                    className="topic-row"
                    key={topic.topic}
                  >

                    <div className="topic-row-top">

                      <span className="topic-name">
                        {topic.topic}
                      </span>

                      <span className="topic-progress">
                        {topic.solved}/
                        {topic.total}
                      </span>

                    </div>


                    <div className="topic-progress-bar">

                      <div
                        className="topic-progress-fill"
                        style={{
                          width:
                            `${topic.progress}%`
                        }}
                      />

                    </div>


                    <span className="topic-percent">
                      {topic.progress}%
                      {" "}completed
                    </span>

                  </div>

                ))

            ) : (

              <div className="topics-empty">

                <div className="topic-circle">
                  <Target size={19} />
                </div>

                <h3>
                  Start exploring
                </h3>

                <p>
                  Your topic strengths will appear
                  after solving problems.
                </p>

              </div>

            )}

          </div>

        </section>

      </div>


      {/* =========================
          AI RECOMMENDATIONS
      ========================== */}

      <section className="ai-section">

        <div className="card-header">

          <div className="card-title">

            <Bot size={17} />

            AI Recommendations

            <span className="ai-pill">

              <Sparkles size={11} />

              AI Powered

            </span>

          </div>

        </div>


        <div className="recommendation-grid">


          <div className="recommendation">

            <div className="recommendation-icon">

              <Trophy size={17} />

            </div>


            <div>

              <span>
                RECOMMENDED NEXT
              </span>

              <h3>
                Master Arrays
              </h3>

              <p>
                Start with Two Sum, Binary Search
                and basic array patterns.
              </p>


              <button
                onClick={() =>
                  navigate("/Problems")
                }
              >

                Practice problems

                <ArrowRight size={12} />

              </button>

            </div>

          </div>


          <div className="recommendation">

            <div className="recommendation-icon">

              <Bot size={17} />

            </div>


            <div>

              <span>
                AI COACH
              </span>

              <h3>
                Need help?
              </h3>

              <p>
                Ask CodePrep AI about DSA concepts,
                code errors or complexity.
              </p>


              <button
                onClick={() =>
                  navigate("/assistant")
                }
              >

                Ask AI

                <ArrowRight size={12} />

              </button>

            </div>

          </div>


        </div>

      </section>

    </div>

  );
}


export default Dashboard;