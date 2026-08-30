import { useEffect, useState } from "react";
import {
  Activity,
  BarChart3,
  CheckCircle2,
  Target,
  TrendingUp,
  XCircle
} from "lucide-react";

import { useNavigate } from "react-router-dom";

import "./Analytics.css";


function Analytics() {

  const navigate = useNavigate();

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);


  useEffect(() => {

    const fetchAnalytics = async () => {

      const token = localStorage.getItem("access");


      if (!token) {
        navigate("/login");
        return;
      }


      try {

        const response = await fetch(
          "http://127.0.0.1:8000/api/problems/analytics/",
          {
            method: "GET",

            headers: {
              "Authorization": `Bearer ${token}`,
            },
          }
        );


        const result = await response.json();

        console.log(
          "ANALYTICS:",
          result
        );


        // Token expired / invalid
        if (response.status === 401) {

          localStorage.removeItem("access");
          localStorage.removeItem("refresh");
          localStorage.removeItem("user");

          navigate("/login");

          return;
        }


        if (!response.ok) {

          throw new Error(
            result.message ||
            "Failed to load analytics"
          );

        }


        setData(result);


      } catch (error) {

        console.error(
          "Analytics error:",
          error
        );

      } finally {

        setLoading(false);

      }

    };


    fetchAnalytics();

  }, [navigate]);


  if (loading) {

    return (
      <div className="analytics-page">

        <h2>
          Loading analytics...
        </h2>

      </div>
    );

  }


  if (!data) {

    return (
      <div className="analytics-page">

        <h2>
          Unable to load analytics.
        </h2>

      </div>
    );

  }


  return (

    <div className="analytics-page">


      {/* HEADER */}

      <div className="analytics-header">

        <div>

          <span className="dashboard-eyebrow">
            PERFORMANCE OVERVIEW
          </span>

          <h1>
            Your Analytics
          </h1>

          <p>
            Track your DSA progress and coding performance.
          </p>

        </div>

      </div>


      {/* OVERVIEW CARDS */}

      <div className="analytics-stats">


        <div className="analytics-stat">

          <div className="analytics-stat-icon">
            <CheckCircle2 size={19} />
          </div>

          <span>
            Problems Solved
          </span>

          <strong>
            {data.solved_problems}
          </strong>

          <small>
            of {data.total_problems} problems
          </small>

        </div>


        <div className="analytics-stat">

          <div className="analytics-stat-icon">
            <Activity size={19} />
          </div>

          <span>
            Problems Attempted
          </span>

          <strong>
            {data.attempted_problems}
          </strong>

          <small>
            unique problems
          </small>

        </div>


        <div className="analytics-stat">

          <div className="analytics-stat-icon">
            <Target size={19} />
          </div>

          <span>
            Accuracy
          </span>

          <strong>
            {data.accuracy}%
          </strong>

          <small>
            submission success rate
          </small>

        </div>


        <div className="analytics-stat">

          <div className="analytics-stat-icon">
            <TrendingUp size={19} />
          </div>

          <span>
            Total Submissions
          </span>

          <strong>
            {data.total_submissions}
          </strong>

          <small>
            all attempts
          </small>

        </div>

      </div>


      {/* MAIN GRID */}

      <div className="analytics-grid">


        {/* DIFFICULTY */}

        <section className="analytics-card">

          <div className="analytics-card-header">

            <div className="analytics-title">

              <BarChart3 size={17} />

              Difficulty Progress

            </div>

          </div>


          <div className="difficulty-list">

            {data.difficulty_stats.map(
              (item) => {

                const percentage =
                  item.total > 0
                    ? Math.round(
                        (item.solved /
                          item.total) *
                        100
                      )
                    : 0;


                return (

                  <div
                    className="difficulty-row"
                    key={item.difficulty}
                  >

                    <div className="difficulty-info">

                      <span
                        className={`difficulty-dot ${item.difficulty.toLowerCase()}`}
                      />

                      <strong>
                        {item.difficulty}
                      </strong>

                      <span>
                        {item.solved}/
                        {item.total}
                      </span>

                    </div>


                    <div className="progress-track">

                      <div
                        className="progress-fill"
                        style={{
                          width:
                            `${percentage}%`
                        }}
                      />

                    </div>


                    <span className="percentage">
                      {percentage}%
                    </span>

                  </div>

                );

              }
            )}

          </div>

        </section>


        {/* SUBMISSION BREAKDOWN */}

        <section className="analytics-card">

          <div className="analytics-card-header">

            <div className="analytics-title">

              <Activity size={17} />

              Submission Breakdown

            </div>

          </div>


          <div className="submission-breakdown">


            <div>

              <CheckCircle2 size={18} />

              <span>
                Accepted
              </span>

              <strong>
                {data.accepted}
              </strong>

            </div>


            <div>

              <XCircle size={18} />

              <span>
                Wrong Answer
              </span>

              <strong>
                {data.wrong_answers}
              </strong>

            </div>


            <div>

              <XCircle size={18} />

              <span>
                Compilation Errors
              </span>

              <strong>
                {data.compilation_errors}
              </strong>

            </div>


            <div>

              <XCircle size={18} />

              <span>
                Runtime Errors
              </span>

              <strong>
                {data.runtime_errors}
              </strong>

            </div>

          </div>

        </section>

      </div>


      {/* TOPIC PROGRESS */}

      <section className="analytics-card topic-card">

        <div className="analytics-card-header">

          <div className="analytics-title">

            <Target size={17} />

            Topic Progress

          </div>

        </div>


        <div className="topic-list">

          {data.topic_stats.map(
            (item) => {

              const percentage =
                item.total > 0
                  ? Math.round(
                      (item.solved /
                        item.total) *
                      100
                    )
                  : 0;


              return (

                <div
                  className="topic-row"
                  key={item.topic}
                >

                  <div className="topic-info">

                    <strong>
                      {item.topic}
                    </strong>

                    <span>
                      {item.solved} /{" "}
                      {item.total} solved
                    </span>

                  </div>


                  <div className="topic-progress">

                    <div
                      style={{
                        width:
                          `${percentage}%`
                      }}
                    />

                  </div>


                  <span className="topic-percentage">
                    {percentage}%
                  </span>

                </div>

              );

            }
          )}

        </div>

      </section>


      {/* RECENT ACTIVITY */}

      <section className="analytics-card">

        <div className="analytics-card-header">

          <div className="analytics-title">

            <Activity size={17} />

            Recent Activity

          </div>

        </div>


        {data.recent_submissions.length === 0 ? (

          <div className="analytics-empty">

            <Activity size={25} />

            <h3>
              No submissions yet
            </h3>

            <p>
              Start solving problems to see your activity here.
            </p>

          </div>

        ) : (

          <div className="activity-list">

            {data.recent_submissions.map(
              (submission, index) => (

                <div
                  className="activity-row"
                  key={index}
                >

                  <div>

                    <strong>
                      {submission.problem}
                    </strong>

                    <span>
                      {submission.topic} •{" "}
                      {submission.difficulty}
                    </span>

                  </div>


                  <span
                    className={`activity-status ${submission.status
                      .toLowerCase()
                      .replaceAll(" ", "-")}`}
                  >
                    {submission.status}
                  </span>

                </div>

              )
            )}

          </div>

        )}

      </section>

    </div>

  );

}


export default Analytics;