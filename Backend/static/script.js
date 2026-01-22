function analyzeReview() {
    const reviewText = document.getElementById("review").value;

    if (!reviewText.trim()) {
        alert("Please enter a review");
        return;
    }

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ review: reviewText })
    })
    .then(response => response.json())
    .then(data => {
        const resultEl = document.getElementById("result");

        resultEl.innerText =
            `Result: ${data.label} (Score: ${data.score.toFixed(2)})`;

        if (data.label.toLowerCase().includes("fake")) {
            resultEl.className = "fake";
        } else {
            resultEl.className = "genuine";
        }

        loadHistory();
    });
}

function loadHistory() {
    fetch("/history")
        .then(response => response.json())
        .then(data => {
            const historyDiv = document.getElementById("history");
            historyDiv.innerHTML = "";

            data.forEach(item => {
                const div = document.createElement("div");
                div.innerText =
                    `${item.label} (${item.score.toFixed(2)}): ${item.text}`;
                historyDiv.appendChild(div);
            });
        });
}

function clearHistory() {
    fetch("/clear", { method: "POST" })
        .then(() => {
            loadHistory();
        });
}

loadHistory();
