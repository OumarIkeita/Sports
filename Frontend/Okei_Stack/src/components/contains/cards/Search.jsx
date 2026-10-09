import { useState } from "react";
import axios from "axios";
import './search.css'
export default function Search() {
  const [query, setQuery] = useState("");
  const [club, setClub] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async (e) => {
    e.preventDefault();

    if (!query.trim()) {
      setError("Please enter a club ID or name.");
      setClub(null);
      return;
    }

    setLoading(true);
    setError("");
    setClub(null);

    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/clubIs/${encodeURIComponent(query.trim())}/`,
      );

      setClub(response.data);
    } catch (err) {
      if (err.response?.status === 404) {
        setError("Club not found.");
      } else {
        setError("Something went wrong. Check your Django server.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="club-search">
      <h2>Search Football Club</h2>

      <form onSubmit={handleSearch}>
        <input
          type="search"
          placeholder="Enter club ID or name..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />

        <button type="submit" disabled={loading}>
          {loading ? "Searching..." : "Search"}
        </button>
      </form>

      {error && <p className="error">{error}</p>}

      {club && (
        <div className="club-result">
          <h3>{club.name}</h3>

          <p>
            <strong>Club ID:</strong> {club.club_id}
          </p>

          {Object.entries(club).map(([key, value]) => (
            <p key={key}>
              <strong>{key.replaceAll("_", " ")}:</strong>{" "}
              {value === null ? "N/A" : String(value)}
            </p>
          ))}
        </div>
      )}
    </div>
  );
}
