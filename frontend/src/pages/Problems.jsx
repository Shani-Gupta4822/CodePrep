import { useEffect, useMemo, useState } from "react";

import {
  Search,
  CheckCircle2,
  ChevronRight,
  SlidersHorizontal,
} from "lucide-react";

import { useNavigate } from "react-router-dom";
import axios from "axios";

import "./Problems.css";


function Problems() {

  const navigate = useNavigate();

  // =========================
  // API DATA
  // =========================

  const [problems, setProblems] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");


  // =========================
  // FILTER STATES
  // =========================

  const [search, setSearch] = useState("");

  const [difficulty, setDifficulty] = useState("All");

  const [topic, setTopic] = useState("All");

  const [status, setStatus] = useState("All");


  // =========================
  // FETCH PROBLEMS
  // =========================

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/api/problems/")

      .then((response) => {

        setProblems(response.data);

        setLoading(false);

      })

      .catch((err) => {

        console.error("Error fetching problems:", err);

        setError("Unable to load problems.");

        setLoading(false);

      });

  }, []);


  // =========================
  // SOLVED PROBLEMS
  // =========================

  const solvedProblems = JSON.parse(
    localStorage.getItem("solvedProblems") || "[]"
  );


  // =========================
  // FILTER PROBLEMS
  // =========================

  const filteredProblems = useMemo(() => {

    return problems.filter((problem) => {

      const matchesSearch =
        problem.title
          .toLowerCase()
          .includes(search.toLowerCase()) ||

        problem.topic
          .toLowerCase()
          .includes(search.toLowerCase());


      const matchesDifficulty =
        difficulty === "All" ||
        problem.difficulty === difficulty;


      const matchesTopic =
        topic === "All" ||
        problem.topic === topic;


      const isSolved =
        solvedProblems.includes(problem.id);


      const matchesStatus =
        status === "All" ||

        (status === "Solved" && isSolved) ||

        (status === "Unsolved" && !isSolved);


      return (
        matchesSearch &&
        matchesDifficulty &&
        matchesTopic &&
        matchesStatus
      );

    });

  }, [
    problems,
    search,
    difficulty,
    topic,
    status,
    solvedProblems,
  ]);


  // =========================
  // STATISTICS
  // =========================

  const totalProblems = problems.length;

  const easyProblems = problems.filter(
    (problem) => problem.difficulty === "Easy"
  ).length;

  const mediumProblems = problems.filter(
    (problem) => problem.difficulty === "Medium"
  ).length;

  const hardProblems = problems.filter(
    (problem) => problem.difficulty === "Hard"
  ).length;


  // =========================
  // TOPICS
  // =========================

  const topics = [
    ...new Set(
      problems.map((problem) => problem.topic)
    ),
  ];


  // =========================
  // LOADING
  // =========================

  if (loading) {

    return (

      <div className="problems-page">

        <div className="problems-header">

          <div>

            <span className="page-eyebrow">
              PRACTICE ARENA
            </span>

            <h1>
              Problems
            </h1>

            <p>
              Loading coding problems...
            </p>

          </div>

        </div>

      </div>

    );

  }


  // =========================
  // ERROR
  // =========================

  if (error) {

    return (

      <div className="problems-page">

        <div className="problems-header">

          <div>

            <span className="page-eyebrow">
              PRACTICE ARENA
            </span>

            <h1>
              Problems
            </h1>

            <p>
              {error}
            </p>

          </div>

        </div>

      </div>

    );

  }


  // =========================
  // UI
  // =========================

  return (

    <div className="problems-page">


      {/* =========================
          HEADER
      ========================== */}

      <div className="problems-header">

        <div>

          <span className="page-eyebrow">
            PRACTICE ARENA
          </span>

          <h1>
            Problems
          </h1>

          <p>
            Sharpen your DSA skills with
            interview-focused problems.
          </p>

        </div>


        {/* PROBLEM STATISTICS */}

        <div className="problem-stats">

          <div>

            <strong>
              {totalProblems}
            </strong>

            <span>
              Total
            </span>

          </div>


          <div>

            <strong>
              {easyProblems}
            </strong>

            <span>
              Easy
            </span>

          </div>


          <div>

            <strong>
              {mediumProblems}
            </strong>

            <span>
              Medium
            </span>

          </div>


          <div>

            <strong>
              {hardProblems}
            </strong>

            <span>
              Hard
            </span>

          </div>

        </div>

      </div>


      {/* =========================
          FILTER BAR
      ========================== */}

      <div className="filters">


        {/* SEARCH */}

        <div className="problem-search">

          <Search size={16} />

          <input
            type="text"
            placeholder="Search problems..."
            value={search}
            onChange={(e) =>
              setSearch(e.target.value)
            }
          />

        </div>


        {/* DIFFICULTY */}

        <div className="filter-select">

          <SlidersHorizontal size={14} />

          <select
            value={difficulty}
            onChange={(e) =>
              setDifficulty(e.target.value)
            }
          >

            <option value="All">
              Difficulty
            </option>

            <option value="Easy">
              Easy
            </option>

            <option value="Medium">
              Medium
            </option>

            <option value="Hard">
              Hard
            </option>

          </select>

        </div>


        {/* TOPIC */}

        <div className="filter-select">

          <select
            value={topic}
            onChange={(e) =>
              setTopic(e.target.value)
            }
          >

            <option value="All">
              Topic
            </option>


            {topics.map((currentTopic) => (

              <option
                key={currentTopic}
                value={currentTopic}
              >
                {currentTopic}
              </option>

            ))}

          </select>

        </div>


        {/* STATUS */}

        <div className="filter-select">

          <select
            value={status}
            onChange={(e) =>
              setStatus(e.target.value)
            }
          >

            <option value="All">
              Status
            </option>

            <option value="Solved">
              Solved
            </option>

            <option value="Unsolved">
              Unsolved
            </option>

          </select>

        </div>

      </div>


      {/* =========================
          PROBLEM TABLE
      ========================== */}

      <div className="problem-table">


        {/* TABLE HEADER */}

        <div className="table-head">

          <span>
            Status
          </span>

          <span>
            Problem
          </span>

          <span>
            Difficulty
          </span>

          <span>
            Acceptance
          </span>

          <span></span>

        </div>


        {/* PROBLEMS */}

        {filteredProblems.length > 0 ? (

          filteredProblems.map((problem) => {

            const isSolved =
              solvedProblems.includes(problem.id);


            return (

              <div
                className="problem-row"
                key={problem.id}

                onClick={() =>
                  navigate(
                    `/problems/${problem.id}`
                  )
                }
              >


                {/* STATUS */}

                <div className="problem-status">

                  {isSolved ? (

                    <CheckCircle2
                      size={18}
                      className="solved-icon"
                    />

                  ) : (

                    <div className="unsolved-circle"></div>

                  )}

                </div>


                {/* TITLE */}

                <div className="problem-title">

                  <strong>
                    {problem.title}
                  </strong>

                  <span>
                    {problem.topic}
                  </span>

                </div>


                {/* DIFFICULTY */}

                <div>

                  <span
                    className={
                      `difficulty ${problem.difficulty.toLowerCase()}`
                    }
                  >

                    {problem.difficulty}

                  </span>

                </div>


                {/* ACCEPTANCE */}

                <div className="acceptance">

                  {problem.acceptance}%

                </div>


                {/* ARROW */}

                <ChevronRight
                  size={17}
                  className="row-arrow"
                />

              </div>

            );

          })

        ) : (

          <div className="no-results">

            <Search size={25} />

            <strong>
              No problems found
            </strong>

            <span>
              Try changing your search or filters.
            </span>

          </div>

        )}

      </div>


      {/* =========================
          FOOTER
      ========================== */}

      <div className="problem-count">

        Showing{" "}

        <strong>
          {filteredProblems.length}
        </strong>

        {" "}of{" "}

        {problems.length}

        {" "}problems

      </div>


    </div>

  );

}


export default Problems;