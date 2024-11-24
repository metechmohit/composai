document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-btn');
    const editor = document.getElementById('editor');
    const copyBtn = document.getElementById('copy-btn');
    const downloadBtn = document.getElementById('download-btn');
    const regenerateBtn = document.getElementById('regenerate-btn');

    generateBtn.addEventListener('click', async () => {
        const topic = document.getElementById('topic').value;
        const keywords = document.getElementById('keywords').value;
        const tone = document.getElementById('tone').value;
        const length = document.getElementById('length').value;

        // Show loading state
        editor.innerHTML = '<div class="loading">Generating content...</div>';
        generateBtn.disabled = true;

        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    topic,
                    keywords,
                    tone,
                    length
                })
            });

            const data = await response.json();

            if (data.status === 'success') {
                editor.innerHTML = data.content;
            } else {
                editor.innerHTML = `Error: ${data.message}`;
            }
        } catch (error) {
            editor.innerHTML = 'Error generating content. Please try again.';
        } finally {
            generateBtn.disabled = false;
        }
    });

    copyBtn.addEventListener('click', () => {
        const content = editor.innerText;
        navigator.clipboard.writeText(content);
        alert('Content copied to clipboard!');
    });

    downloadBtn.addEventListener('click', () => {
        const content = editor.innerText;
        const blob = new Blob([content], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'generated-content.txt';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    });

    regenerateBtn.addEventListener('click', () => {
        generateBtn.click();
    });
});