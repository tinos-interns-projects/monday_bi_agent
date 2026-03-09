from flask import Flask, request, jsonify, render_template
from agent.ai_agent import handle_query
from utils.tool_trace import get_trace, clear_trace, add_trace


# Tell Flask where templates and static files are located
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


# ----------------------------------
# Home route → loads chat interface
# ----------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------------
# Health check route
# ----------------------------------
@app.route("/status")
def status():

    add_trace("Status check called")

    return jsonify({
        "message": "Monday BI Agent Running",
        "status": "OK"
    })


# ----------------------------------
# Main AI Query Endpoint
# ----------------------------------
@app.route("/ask", methods=["POST"])
def ask():

    try:

        # Check JSON input
        if not request.is_json:
            return jsonify({
                "error": "Request must be JSON"
            }), 400

        data = request.get_json()

        # Validate input
        if not data or "query" not in data:
            return jsonify({
                "error": "Query not provided"
            }), 400

        query = data["query"]

        if not query or not isinstance(query, str):
            return jsonify({
                "error": "Invalid query"
            }), 400

        add_trace(f"Received query: {query}")

        # Clear previous trace
        clear_trace()

        # Run AI agent
        answer = handle_query(query)

        # Collect tool trace
        trace = get_trace()

        return jsonify({
            "query": query,
            "answer": answer,
            "trace": trace
        })

    except Exception as e:

        add_trace(f"Server error: {str(e)}")

        return jsonify({
            "error": str(e)
        }), 500


# ----------------------------------
# Run server
# ----------------------------------
if __name__ == "__main__":

    print("🚀 Monday BI Agent Server Starting...")
    print("🌐 Open: http://127.0.0.1:5000")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )