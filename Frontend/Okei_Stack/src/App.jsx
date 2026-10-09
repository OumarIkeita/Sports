import React from "react";
import axios from "axios";
import { useState, useEffect } from "react";
import RouterNav from "./components/navbar/RouterNav";

export default function App() {
  return (
    <>
      <RouterNav />
    </>
  );
}

/*
  const [students, setStudents] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/courses/")
      .then((response) => {
        setStudents(response.data);
      })
      .catch(console.error());
  }, []);
  return (
    <div>
      <>
        <h1>Course Informations</h1>
        {students.map((student) => {
          return (
            <div key={student.id}>
              <h2>{student.course_code}</h2>
            </div>
          );
        })}
      
*/
