import { NavLink } from "react-router-dom";

import {
  LayoutDashboard,
  Code2,
  Bot,
  FileText,
  Route,
  Users,
  BarChart3,
  Settings,
  Zap
} from "lucide-react";


const menuItems = [
  {
    name: "Dashboard",
    path: "/",
    icon: LayoutDashboard
  },
  {
    name: "Problems",
    path: "/problems",
    icon: Code2
  },
  {
    name: "Assistant",
    path: "/assistant",
    icon: Bot
  },
  {
    name: "Resume",
    path: "/resume",
    icon: FileText
  },
  {
    name: "Roadmap",
    path: "/roadmap",
    icon: Route
  },
  {
    name: "Mock Interview",
    path: "/mock-interview",
    icon: Users
  },
  {
    name: "Analytics",
    path: "/analytics",
    icon: BarChart3
  }
];


function Sidebar() {

  return (
    <aside className="sidebar">

      {/* Logo */}

      <div className="brand">

        <div className="brand-icon">
          <Zap size={17} />
        </div>

        <span>
          CodePrep <b>AI</b>
        </span>

      </div>


      {/* Navigation */}

      <nav className="sidebar-nav">

        {menuItems.map((item) => {

          const Icon = item.icon;

          return (
            <NavLink
              key={item.path}
              to={item.path}
              end={item.path === "/"}
              className={({ isActive }) =>
                isActive
                  ? "nav-item active"
                  : "nav-item"
              }
            >

              <Icon size={17} />

              <span>
                {item.name}
              </span>

            </NavLink>
          );

        })}

      </nav>


      {/* Bottom profile */}

      <div className="sidebar-bottom">

        <div className="profile">

          <div className="avatar">
            SG
          </div>

          <div>

            <strong>
              Shani Gupta
            </strong>

            <span>
              Candidate
            </span>

          </div>

        </div>


        <button className="settings-btn">

          <Settings size={16} />

          Settings

        </button>

      </div>

    </aside>
  );
}


export default Sidebar;