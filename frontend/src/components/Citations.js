import React from "react";

function Citations({ citations }) {
  return (
    <div>
      <h2>📚 Citations</h2>
      
      <h3>APA</h3>
      <ul>
        {citations.APA.map((c, i) => (
          <li key={i}>{c}</li>
        ))}
      </ul>

      <h3>MLA</h3>
      <ul>
        {citations.MLA.map((c, i) => (
          <li key={i}>{c}</li>
        ))}
      </ul>

      <h3>IEEE</h3>
      <ul>
        {citations.IEEE.map((c, i) => (
          <li key={i}>{c}</li>
        ))}
      </ul>
    </div>
  );
}

export default Citations;
