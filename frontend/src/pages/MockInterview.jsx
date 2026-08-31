import { useState } from "react";
import {
  ArrowRight,
  Bot,
  CheckCircle2,
  RotateCcw,
  Trophy
} from "lucide-react";

import "./MockInterview.css";

function MockInterview() {

  const [started, setStarted] = useState(false);
  const [loading, setLoading] = useState(false);

  const [topic, setTopic] = useState("DSA");
  const [level, setLevel] = useState("Beginner");

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const [feedback, setFeedback] = useState(null);

  const [questionNumber, setQuestionNumber] = useState(1);
  const [score, setScore] = useState(0);

  const [finished, setFinished] = useState(false);


  // =========================
  // START INTERVIEW
  // =========================

  const startInterview = async () => {

    setLoading(true);

    try {

      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/api/problems/mock-interview/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            action: "start",
            topic,
            level,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message || "Failed to start interview");
      }

      setQuestion(data.question);
      setStarted(true);
      setFeedback(null);

    } catch (error) {

      console.error(error);
      alert("Failed to start interview.");

    } finally {

      setLoading(false);

    }
  };


  // =========================
  // SUBMIT ANSWER
  // =========================

  const submitAnswer = async () => {

    if (!answer.trim()) {
      alert("Please write your answer.");
      return;
    }

    setLoading(true);

    try {

      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/api/problems/mock-interview/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            action: "evaluate",
            topic,
            level,
            question,
            answer,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message || "Evaluation failed");
      }

      setFeedback(data);

      setScore((prev) => prev + (data.score || 0));

    } catch (error) {

      console.error(error);
      alert("Failed to evaluate answer.");

    } finally {

      setLoading(false);

    }
  };


  // =========================
  // NEXT QUESTION
  // =========================

  const nextQuestion = async () => {

    if (questionNumber >= 5) {

      setFinished(true);
      return;

    }

    setLoading(true);

    try {

      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/api/problems/mock-interview/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            action: "next",
            topic,
            level,
            previous_question: question,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message || "Failed to get next question");
      }

      setQuestion(data.question);
      setQuestionNumber((prev) => prev + 1);

      setAnswer("");
      setFeedback(null);

    } catch (error) {

      console.error(error);
      alert("Failed to load next question.");

    } finally {

      setLoading(false);

    }
  };


  // =========================
  // RESET
  // =========================

  const restartInterview = () => {

    setStarted(false);
    setFinished(false);
    setQuestion("");
    setAnswer("");
    setFeedback(null);
    setQuestionNumber(1);
    setScore(0);

  };


  // =========================
  // FINAL RESULT
  // =========================

  if (finished) {

    const finalScore = Math.round(score / 5);

    return (

      <div className="mock-page">

        <div className="mock-result">

          <div className="result-icon">
            <Trophy size={34} />
          </div>

          <span className="dashboard-eyebrow">
            INTERVIEW COMPLETE
          </span>

          <h1>
            Great job!
          </h1>

          <p>
            Here's your mock interview performance.
          </p>

          <div className="final-score">

            <strong>
              {finalScore}
            </strong>

            <span>
              / 20
            </span>

          </div>

          <div className="result-message">

            {finalScore >= 15
              ? "Excellent performance. You are interview ready!"
              : finalScore >= 10
              ? "Good attempt. Keep practicing your weak areas."
              : "Keep practicing. Focus on fundamentals and explanation."
            }

          </div>

          <button
            className="primary-btn"
            onClick={restartInterview}
          >

            <RotateCcw size={15} />

            Start New Interview

          </button>

        </div>

      </div>

    );
  }


  // =========================
  // START SCREEN
  // =========================

  if (!started) {

    return (

      <div className="mock-page">

        <div className="mock-header">

          <span className="dashboard-eyebrow">
            AI POWERED
          </span>

          <h1>
            Mock Interview
          </h1>

          <p>
            Practice real interview questions with your AI interviewer.
          </p>

        </div>


        <div className="mock-setup">

          <div className="setup-icon">
            <Bot size={28} />
          </div>

          <h2>
            Configure your interview
          </h2>

          <p>
            Choose your topic and difficulty level.
          </p>


          <label>
            Interview Topic
          </label>

          <select
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
          >

            <option>DSA</option>
            <option>Java</option>
            <option>System Design</option>
            <option>DBMS</option>
            <option>Computer Networks</option>

          </select>


          <label>
            Difficulty
          </label>

          <select
            value={level}
            onChange={(e) => setLevel(e.target.value)}
          >

            <option>Beginner</option>
            <option>Intermediate</option>
            <option>Advanced</option>

          </select>


          <button
            className="primary-btn mock-start"
            onClick={startInterview}
            disabled={loading}
          >

            {loading ? "Starting..." : "Start Interview"}

            <ArrowRight size={16} />

          </button>

        </div>

      </div>

    );
  }


  // =========================
  // INTERVIEW SCREEN
  // =========================

  return (

    <div className="mock-page">

      <div className="interview-top">

        <div>

          <span className="dashboard-eyebrow">
            AI MOCK INTERVIEW
          </span>

          <h1>
            Question {questionNumber} of 5
          </h1>

        </div>

        <div className="interview-topic">
          {topic} • {level}
        </div>

      </div>


      <div className="progress-bar">

        <div
          style={{
            width: `${(questionNumber / 5) * 100}%`
          }}
        />

      </div>


      <div className="question-card">

        <div className="question-icon">
          <Bot size={20} />
        </div>

        <div>

          <span>
            INTERVIEWER
          </span>

          <h2>
            {question}
          </h2>

        </div>

      </div>


      {!feedback ? (

        <div className="answer-card">

          <label>
            Your Answer
          </label>

          <textarea
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            placeholder="Explain your approach clearly..."
          />

          <button
            className="primary-btn"
            onClick={submitAnswer}
            disabled={loading}
          >

            {loading ? "Evaluating..." : "Submit Answer"}

            <ArrowRight size={15} />

          </button>

        </div>

      ) : (

        <div className="feedback-card">

          <div className="feedback-header">

            <div>
              <CheckCircle2 size={20} />
              AI Evaluation
            </div>

            <strong>
              {feedback.score}/20
            </strong>

          </div>


          <div className="feedback-section">

            <h3>
              Feedback
            </h3>

            <p>
              {feedback.feedback}
            </p>

          </div>


          <div className="feedback-section">

            <h3>
              Correct Approach
            </h3>

            <p>
              {feedback.correct_approach}
            </p>

          </div>


          <button
            className="primary-btn"
            onClick={nextQuestion}
            disabled={loading}
          >

            {questionNumber >= 5
              ? "Finish Interview"
              : "Next Question"
            }

            <ArrowRight size={15} />

          </button>

        </div>

      )}

    </div>

  );
}

export default MockInterview;