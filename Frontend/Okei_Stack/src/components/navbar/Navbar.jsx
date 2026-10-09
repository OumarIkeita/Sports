import React from "react";
import { Link } from "react-router-dom";
import "./navbar.css";
export default function Navbar() {
  return (
    <div className="MainDiv">
      <div className="navbarDiv">
        <ul className="ulList">
          <li>
            <Link to={"/"}>HOME</Link>
          </li>
          <li>
            <Link to={"/Team_sport"}>Team_sport</Link>
          </li>
          <li>
            <Link to={"/Combat_sport"}>Combat_sport</Link>
          </li>
          <li>
            <Link to={"/Net_sport"}>Net_sport</Link>
          </li>
          <li>
            <Link to={"/Track_field"}>Track_field</Link>
          </li>
          <li>
            <Link to={"/Precision_sport"}>Precision_sport</Link>
          </li>
        </ul>
      </div>
    </div>
  );
}
