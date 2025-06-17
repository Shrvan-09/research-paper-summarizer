import React from "react";

function UploadForm({ setData }) {
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:8000/upload/", {
      method: "POST",
      body: formData,
    });

    const result = await res.json();
    setData(result);
  };

  return (
    <div>
      <h2>Upload PDF</h2>
      <input type="file" onChange={handleUpload} />
    </div>
  );
}

export default UploadForm;
