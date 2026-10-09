import React from "react";
import axios from "axios";
import { useState, useEffect } from "react";
import Card from "../cards/Card";
export default function Club() {
  const [club, setClub] = useState([]);
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/clubs/")
      .then((response) => setClub(response.data));
  }, []);
  return (
    <div>
      <Card club={club} />
    </div>
  );
}
