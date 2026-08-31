import { useState } from "react";
import {
  Upload,
  FileText,
  CheckCircle2,
  AlertCircle,
  Sparkles,
  Target,
  Briefcase,
  ArrowUp,
  X
} from "lucide-react";

import "./Resume.css";

function Resume() {

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {

    const selectedFile = e.target.files[0];

    if (!selectedFile) return;

    if (selectedFile.type !== "application/pdf") {
      alert("Please upload a PDF file.");
      return;
    }

    setFile(selectedFile);
    setResult(null);
  };


  const analyzeResume = async () => {

    if (!file) {
      alert("Please upload your resume first.");
      return;
    }

    setLoading(true);

    const formData = new FormData();

    formData.append("resume", file);

    try {

      const response = await fetch(
       `${import.meta.env.VITE_API_URL}/api/problems/resume/analyze/`,
        {
          method: "POST",
          body: formData
        }
      );

      const data = await response.json();

      console.log("RESUME ANALYSIS:", data);

      if (!response.ok) {
        throw new Error(
          data.message || "Resume analysis failed"
        );
      }

      setResult(data);

    } catch (error) {

      console.error("Resume analysis error:", error);

      alert("Resume analysis failed.");

    } finally {

      setLoading(false);

    }
  };


  const removeFile = () => {
    setFile(null);
    setResult(null);
  };


  return (

    <div className="resume-page">

      {/* HEADER */}

      <div className="resume-header">

        <div>

          <span className="resume-eyebrow">
            AI POWERED
          </span>

          <h1>
            Resume Analyzer
          </h1>

          <p>
            Analyze your resume and improve your chances
            of getting shortlisted.
          </p>

        </div>

      </div>


      {/* UPLOAD */}

      <section className="resume-upload-card">

        <div className="resume-card-header">

          <div className="resume-card-title">

            <FileText size={18} />

            Upload Resume

          </div>

        </div>


        {!file ? (

          <label className="upload-area">

            <input
              type="file"
              accept=".pdf"
              onChange={handleFileChange}
              hidden
            />

            <div className="upload-icon">
              <Upload size={25} />
            </div>

            <h3>
              Upload your resume
            </h3>

            <p>
              Drag & drop your PDF here or click to browse
            </p>

            <span>
              PDF only • Maximum 5MB
            </span>

          </label>

        ) : (

          <div className="selected-file">

            <div className="selected-file-left">

              <div className="file-icon">
                <FileText size={22} />
              </div>

              <div>

                <strong>
                  {file.name}
                </strong>

                <span>
                  {(file.size / 1024 / 1024).toFixed(2)} MB
                </span>

              </div>

            </div>

            <button
              className="remove-file"
              onClick={removeFile}
            >
              <X size={17} />
            </button>

          </div>

        )}


        <button
          className="analyze-btn"
          onClick={analyzeResume}
          disabled={!file || loading}
        >

          {loading ? (
            <>
              Analyzing Resume...
            </>
          ) : (
            <>
              Analyze Resume
              <Sparkles size={16} />
            </>
          )}

        </button>

      </section>


      {/* RESULT */}

      {result && (

        <section className="analysis-section">

          {/* ATS SCORE */}

          <div className="ats-card">

            <div>

              <span className="result-label">
                ATS SCORE
              </span>

              <h2>
                {result.ats_score}
                <span>/100</span>
              </h2>

              <p>
                {result.ats_message ||
                  "Your resume has been analyzed successfully."}
              </p>

            </div>


            <div className="score-circle">

              <div>
                <strong>
                  {result.ats_score}
                </strong>

                <span>
                  ATS
                </span>
              </div>

            </div>

          </div>


          {/* SCORE CARDS */}

          <div className="score-grid">

            <div className="score-card">

              <div className="score-card-icon">
                <Target size={18} />
              </div>

              <span>
                Keyword Match
              </span>

              <strong>
                {result.keyword_match || 0}%
              </strong>

            </div>


            <div className="score-card">

              <div className="score-card-icon">
                <Briefcase size={18} />
              </div>

              <span>
                Skills Match
              </span>

              <strong>
                {result.skills_match || 0}%
              </strong>

            </div>


            <div className="score-card">

              <div className="score-card-icon">
                <FileText size={18} />
              </div>

              <span>
                Formatting
              </span>

              <strong>
                {result.formatting_score || 0}%
              </strong>

            </div>

          </div>


          {/* SKILLS */}

          <div className="analysis-grid">

            <div className="analysis-card">

              <div className="analysis-title">

                <CheckCircle2 size={17} />

                Detected Skills

              </div>


              <div className="skill-list">

                {(result.skills || []).map(
                  (skill, index) => (

                    <span key={index}>
                      {skill}
                    </span>

                  )
                )}

              </div>

            </div>


            {/* MISSING */}

            <div className="analysis-card">

              <div className="analysis-title">

                <AlertCircle size={17} />

                Recommended Skills

              </div>


              <div className="skill-list missing">

                {(result.missing_skills || []).map(
                  (skill, index) => (

                    <span key={index}>
                      {skill}
                    </span>

                  )
                )}

              </div>

            </div>

          </div>


          {/* STRENGTHS */}

          <div className="analysis-card full-card">

            <div className="analysis-title">

              <ArrowUp size={17} />

              Resume Strengths

            </div>


            <ul>

              {(result.strengths || []).map(
                (item, index) => (

                  <li key={index}>
                    {item}
                  </li>

                )
              )}

            </ul>

          </div>


          {/* IMPROVEMENTS */}

          <div className="analysis-card full-card">

            <div className="analysis-title">

              <AlertCircle size={17} />

              Improvements

            </div>


            <ul>

              {(result.improvements || []).map(
                (item, index) => (

                  <li key={index}>
                    {item}
                  </li>

                )
              )}

            </ul>

          </div>


          {/* AI FEEDBACK */}

          <div className="ai-resume-card">

            <div className="ai-resume-icon">
              <Sparkles size={20} />
            </div>

            <div>

              <span>
                AI RESUME COACH
              </span>

              <h3>
                Personalized Feedback
              </h3>

              <p>
                {result.ai_feedback ||
                  "Your resume analysis is ready."}
              </p>

            </div>

          </div>

        </section>

      )}

    </div>
  );
}

export default Resume;