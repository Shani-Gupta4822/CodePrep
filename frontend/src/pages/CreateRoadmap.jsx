import { useState } from "react";
import { ArrowRight, Route } from "lucide-react";
import { useNavigate } from "react-router-dom";

import "./Roadmap.css";


function CreateRoadmap() {

  const navigate = useNavigate();

  const [goal, setGoal] = useState("Interview Preparation");
  const [level, setLevel] = useState("Beginner");
  const [problemsPerDay, setProblemsPerDay] = useState(2);

  const [loading, setLoading] = useState(false);


  const generateRoadmap = async () => {

    setLoading(true);

    try {

      const token = localStorage.getItem("access");

      if (!token) {
        alert("Please login first.");
        navigate("/login");
        return;
      }


      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/api/problems/roadmap/`,
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
          },

          body: JSON.stringify({
            goal,
            level,
            problems_per_day: problemsPerDay,
          }),
        }
      );


      const data = await response.json();

      console.log("CREATED ROADMAP:", data);


      if (response.status === 401) {

        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        localStorage.removeItem("user");

        alert("Session expired. Please login again.");

        navigate("/login");

        return;
      }


      if (!response.ok) {

        throw new Error(
          data.message || "Failed to create roadmap"
        );

      }


      navigate("/roadmap");


    } catch (error) {

      console.error(
        "Roadmap creation error:",
        error
      );

      alert(
        error.message ||
        "Failed to generate roadmap."
      );


    } finally {

      setLoading(false);

    }
  };


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
          Tell us about your preparation goals.
        </p>


        <div className="roadmap-form">

          <label>
            Your Goal
          </label>


          <select
            value={goal}
            onChange={(e) =>
              setGoal(e.target.value)
            }
          >

            <option>
              Interview Preparation
            </option>

            <option>
              DSA Mastery
            </option>

            <option>
              Placement Preparation
            </option>

          </select>


          <label>
            Your Level
          </label>


          <select
            value={level}
            onChange={(e) =>
              setLevel(e.target.value)
            }
          >

            <option>
              Beginner
            </option>

            <option>
              Intermediate
            </option>

            <option>
              Advanced
            </option>

          </select>


          <label>
            Problems Per Day
          </label>


          <select
            value={problemsPerDay}
            onChange={(e) =>
              setProblemsPerDay(
                Number(e.target.value)
              )
            }
          >

            <option value={1}>
              1 Problem
            </option>

            <option value={2}>
              2 Problems
            </option>

            <option value={3}>
              3 Problems
            </option>

            <option value={5}>
              5 Problems
            </option>

          </select>


          <button
            className="primary-btn"
            onClick={generateRoadmap}
            disabled={loading}
          >

            {loading
              ? "Generating..."
              : "Generate Roadmap"
            }

            {!loading && (
              <ArrowRight size={16} />
            )}

          </button>

        </div>

      </div>

    </div>

  );
}


export default CreateRoadmap;