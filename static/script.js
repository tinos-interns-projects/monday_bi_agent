async function ask() {

    const query = document.getElementById("query").value;

    if (!query) {
        alert("Please enter a question");
        return;
    }

    document.getElementById("response").innerText = "Thinking...";
    document.getElementById("trace").innerText = "";

    try {

        const res = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                query: query
            })
        });

        const data = await res.json();

        // Show answer
        document.getElementById("response").innerText =
            data.answer || "No answer returned";

        // Show trace
        if (data.trace) {
            document.getElementById("trace").innerText =
                JSON.stringify(data.trace, null, 2);
        }

    } catch (error) {

        document.getElementById("response").innerText =
            "Error contacting server";

        console.error(error);
    }
}