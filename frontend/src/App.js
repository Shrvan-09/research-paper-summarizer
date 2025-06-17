import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import Keyphrases from "./components/Keyphrases";

function App() {
  const [data, setData] = useState(null);

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    alert("Copied to clipboard!");
  };

  return (
    <div className="App p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-center">AI Research Paper Summarizer</h1>
      
      <UploadForm setData={setData} />

      {data && (
        <>
          {/* Summary Section */}
          <div className="bg-gray-100 p-4 rounded shadow my-6">
            <h2 className="text-xl font-semibold mb-2">Summary</h2>
            <p>{data.summary}</p>
            <button
              onClick={() => copyToClipboard(data.summary)}
              className="mt-2 bg-blue-500 hover:bg-blue-600 text-white px-4 py-1 rounded"
            >
              Copy Summary
            </button>
          </div>

          {/* Keyphrases */}
          <Keyphrases keyphrases={data.keyphrases} />

          {/* Citations Section */}
          <div className="bg-gray-100 p-4 rounded shadow my-6">
            <h2 className="text-xl font-semibold mb-2">Citations</h2>
            <ul className="list-disc ml-6">
              {data.citations.map((citation, idx) => (
                <li key={idx}>{citation}</li>
              ))}
            </ul>
            <button
              onClick={() => copyToClipboard(data.citations.join("\n"))}
              className="mt-2 bg-green-600 hover:bg-green-700 text-white px-4 py-1 rounded"
            >
              Copy Citations
            </button>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
