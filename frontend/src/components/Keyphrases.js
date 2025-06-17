import React from "react";

function Keyphrases({ keyphrases }) {
  return (
    <div>
      <h2>🔑 Keyphrases</h2>
      <ul>
        {keyphrases.map((phrase, index) => (
          <li key={index}>{phrase}</li>
        ))}
      </ul>
    </div>
  );
}

export default Keyphrases;
