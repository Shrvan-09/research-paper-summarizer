document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('uploadForm');
    const fileInput = document.getElementById('fileInput');
    const summaryOutput = document.getElementById('summaryOutput');
    const citationOutput = document.getElementById('citationOutput');
  
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
  
      const file = fileInput.files[0];
      if (!file) {
        alert('Please select a file.');
        return;
      }
  
      const formData = new FormData();
      formData.append('file', file);
  
      summaryOutput.textContent = '⏳ Processing...';
      citationOutput.textContent = '';
  
      try {
        const response = await fetch('http://127.0.0.1:8000/summarize', {
          method: 'POST',
          body: formData,
        });
  
        const result = await response.json();
  
        if (!response.ok) {
          throw new Error(result.detail || 'Something went wrong.');
        }
  
        summaryOutput.textContent = result.summary || 'No summary generated.';
        citationOutput.textContent = result.citations || 'No citations generated.';
      } catch (err) {
        summaryOutput.textContent = `❌ Error: ${err.message}`;
      }
    });
  });
  