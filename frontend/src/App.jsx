import { Routes, Route, useLocation } from "react-router-dom";

import CreateRoadmap from "./pages/CreateRoadmap";

import Sidebar from "./components/Sidebar";
import Navbar from "./components/Navbar";

import Dashboard from "./pages/Dashboard";
import ProblemDetail from "./pages/ProblemDetail";
import Problems from "./pages/Problems";
import Roadmap from "./pages/Roadmap";
import Resume from "./pages/Resume";
import MockInterview from "./pages/MockInterview";
import Assistant from "./pages/Assistant";
import Analytics from "./pages/Analytics";

import Login from "./pages/Login";
import Signup from "./pages/Signup";
import ProtectedRoute from "./pages/ProtectedRoute";


function App() {

  const location = useLocation();

  const isAuthPage =
    location.pathname === "/login" ||
    location.pathname === "/signup";


  return (

    <div className="app">

      {/* Sidebar only for logged-in app pages */}

      {!isAuthPage && <Sidebar />}


      <div className="main">

        {/* Navbar only for logged-in app pages */}

        {!isAuthPage && <Navbar />}


        <main className="content">

          <Routes>

            {/* =========================
                PUBLIC ROUTES
            ========================== */}

            <Route
              path="/login"
              element={<Login />}
            />

            <Route
              path="/signup"
              element={<Signup />}
            />


            {/* =========================
                PROTECTED ROUTES
            ========================== */}

            <Route element={<ProtectedRoute />}>

              <Route
                path="/"
                element={<Dashboard />}
              />


              <Route
                path="/Problems"
                element={<Problems />}
              />


              <Route
                path="/problems/:id"
                element={<ProblemDetail />}
              />


              <Route
                path="/assistant"
                element={<Assistant />}
              />


              <Route
                path="/resume"
                element={<Resume />}
              />


              <Route
                path="/roadmap"
                element={<Roadmap />}
              />


              <Route
                path="/roadmap/create"
                element={<CreateRoadmap />}
              />


              <Route
                path="/mock-interview"
                element={<MockInterview />}
              />


              <Route
                path="/analytics"
                element={<Analytics />}
              />

            </Route>

          </Routes>

        </main>

      </div>

    </div>

  );
}


export default App;