import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./Navbar";
import Allpages from "../pages/Allpages";
import "./routNav.css";
export default function RouterNav() {
  return (
    <div>
      <div className="Top_Element">
        <Router>
          <Navbar />
          <Routes>
            <Route path="/" element={<Allpages.TeamSport />} />
            <Route path="/Team_sport" element={<Allpages.TeamSport />} />
            <Route path="/Combat_sport" element={<Allpages.CombatSport />} />
            <Route path="/Net_sport" element={<Allpages.NetSport />} />
            <Route path="/Track_field" element={<Allpages.TrackField />} />
            <Route
              path="/Precision_sport"
              element={<Allpages.PrecissionSport />}
            />
          </Routes>
        </Router>
      </div>
      <div className="Center_Element">he</div>
      <div className="Boot_Element">he</div>
    </div>
  );
}
