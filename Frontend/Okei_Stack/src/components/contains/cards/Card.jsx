import Search from "./Search";
import "./Card.css";

export default function Card({ club }) {
  const year = new Date().getFullYear();

  return (
    <>
      <section className="club-container">
        {club.map((cl) => (
          <div className="club-card" key={cl.club_id}>
            {cl.foundation_year !== year ? (
              <>
                <h1 className="club-name">{cl.name}</h1>

                <div className="club-info">
                  <p>
                    <strong>Short name:</strong>
                    <span>{cl.short_name}</span>
                  </p>

                  <p>
                    <strong>Foundation year:</strong>
                    <span>{cl.foundation_year}</span>
                  </p>
                </div>
              </>
            ) : (
              <div className="new-club">
                <h1 className="club-name">{cl.name}</h1>
                This club is new: <span>{cl.foundation_year}</span>
              </div>
            )}
          </div>
        ))}
      </section>

      <section className="search-section">
        <Search />
      </section>
    </>
  );
}
