import { useEffect, useState } from "react";
import { ArrowRight, Route } from "lucide-react";
import { useNavigate } from "react-router-dom";

import "./Roadmap.css";


function Roadmap() {

  const navigate = useNavigate();

  const [roadmap, setRoadmap] = useState(null);
  const [loading, setLoading] = useState(true);


  useEffect(() => {

    const fetchRoadmap = async () => {

      try {

        const token = localStorage.getItem("access");

        if (!token) {
          navigate("/login");
          return;
        }


        const response = await fetch(
          "http://127.0.0.1:8000/api/problems/roadmap/",
          {
            method: "GET",

            headers: {
              "Authorization": `Bearer ${token}`,
            },
          }
        );


        const data = await response.json();

        console.log("ROADMAP:", data);


        if (response.status === 401) {

          localStorage.removeItem("access");
          localStorage.removeItem("refresh");
          localStorage.removeItem("user");

          navigate("/login");

          return;
        }


        if (!response.ok) {
          throw new Error(
            data.message || "Failed to load roadmap"
          );
        }


        setRoadmap(data);


      } catch (error) {

        console.error(
          "Roadmap error:",
          error
        );

      } finally {

        setLoading(false);

      }

    };


    fetchRoadmap();

  }, [navigate]);


  if (loading) {

    return (
      <div className="roadmap-page">
        Loading...
      </div>
    );

  }


  if (!roadmap || !roadmap.exists) {

    return (

      <div className="roadmap-page">

        <div className="roadmap-empty">

          <div className="roadmap-big-icon">
            <Route size={32} />
          </div>

          <h1>
            Create Your Roadmap
          </h1>

          <p>
            Your personalized DSA roadmap will appear here.
          </p>

          <button
            className="primary-btn"
            onClick={() =>
              navigate("/roadmap/create")
            }
          >

            Generate Roadmap

            <ArrowRight size={16} />

          </button>

        </div>

      </div>

    );

  }


  return (

    <div className="roadmap-page">

      <div className="roadmap-header">

        <div>

          <span className="dashboard-eyebrow">
            YOUR LEARNING PATH
          </span>

          <h1>
            {roadmap.goal}
          </h1>

          <p>
            {roadmap.level} •{" "}
            {roadmap.problems_per_day}{" "}
            problems per day
          </p>

        </div>

      </div>


      <div className="roadmap-list">

        {roadmap.roadmap_data.map(
          (problem, index) => (

            <div
              className="roadmap-problem"
              key={problem.problem_id}
            >

              <div className="roadmap-number">
                {index + 1}
              </div>


              <div className="roadmap-problem-content">

                <span className="roadmap-topic">
                  {problem.topic}
                </span>

                <h3>
                  {problem.title}
                </h3>

                <span
                  className={`difficulty ${problem.difficulty.toLowerCase()}`}
                >
                  {problem.difficulty}
                </span>

              </div>


              <button
                className="roadmap-solve"
                onClick={() =>
                  navigate(
                    `/problems/${problem.problem_id}`
                  )
                }
              >

                Solve

                <ArrowRight size={14} />

              </button>

            </div>

          )
        )}

      </div>

    </div>

  );

}


export default Roadmap;