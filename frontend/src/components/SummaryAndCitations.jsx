import React from 'react';

const SummaryAndCitations = ({ summary, citations }) => {
  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    alert("Copied to clipboard!");
  };

  return (
    <div className="p-4 space-y-6">
      <div className="bg-gray-100 p-4 rounded shadow">
        <h2 className="text-xl font-bold mb-2">Summary</h2>
        <p>{summary}</p>
        <button
          onClick={() => copyToClipboard(summary)}
          className="mt-2 bg-blue-500 text-white px-4 py-1 rounded"
        >
          Copy Summary
        </button>
      </div>

      <div className="bg-gray-100 p-4 rounded shadow">
        <h2 className="text-xl font-bold mb-2">Citations</h2>
        <ul className="list-disc ml-5">
          {citations.map((c, idx) => (
            <li key={idx}>{c}</li>
          ))}
        </ul>
        <button
          onClick={() => copyToClipboard(citations.join('\n'))}
          className="mt-2 bg-green-500 text-white px-4 py-1 rounded"
        >
          Copy Citations
        </button>
      </div>
    </div>
  );
};

export default SummaryAndCitations;
