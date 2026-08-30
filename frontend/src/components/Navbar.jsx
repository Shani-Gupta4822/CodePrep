import {
  Search,
  Flame,
  Bell,
  LogOut,
  User
} from "lucide-react";

import { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";


function Navbar() {

  const navigate = useNavigate();

  const [showMenu, setShowMenu] = useState(false);

  const menuRef = useRef(null);

  const user = JSON.parse(
    localStorage.getItem("user") || "{}"
  );


  // Close dropdown when clicking outside
  useEffect(() => {

    const handleClickOutside = (event) => {

      if (
        menuRef.current &&
        !menuRef.current.contains(event.target)
      ) {
        setShowMenu(false);
      }

    };

    document.addEventListener(
      "mousedown",
      handleClickOutside
    );

    return () => {
      document.removeEventListener(
        "mousedown",
        handleClickOutside
      );
    };

  }, []);


  const handleLogout = () => {

    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    localStorage.removeItem("user");

    navigate("/login", {
      replace: true
    });
  };


  return (
    <header className="navbar">

      {/* Search */}

      <div className="navbar-search">

        <Search size={16} />

        <input
          type="text"
          placeholder="Search problems, topics..."
        />

      </div>


      {/* Right side */}

      <div className="navbar-right">

        <div className="streak">

          <Flame size={16} />

          <span>
            0 day streak
          </span>

        </div>


        <Bell size={17} />


        {/* User */}

        <div
          className="navbar-user"
          ref={menuRef}
        >

          <button
            className="navbar-avatar"
            onClick={() => setShowMenu(!showMenu)}
            title="Account"
          >
            SG
          </button>


          {/* Dropdown */}

          {showMenu && (

            <div className="profile-dropdown">

              <div className="profile-info">

                <div className="profile-icon">
                  <User size={18} />
                </div>

                <div>

                  <strong>
                    {user.username || "User"}
                  </strong>

                  <span>
                    {user.email || "Candidate"}
                  </span>

                </div>

              </div>


              <div className="dropdown-divider"></div>


              <button
                className="logout-button"
                onClick={handleLogout}
              >

                <LogOut size={16} />

                <span>
                  Logout
                </span>

              </button>

            </div>

          )}

        </div>

      </div>

    </header>
  );
}


export default Navbar;