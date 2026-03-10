# Monday Insight Agent
AI-Powered Business Intelligence Agent for monday.com

Monday Insight Agent is an AI-powered analytics assistant that connects with monday.com boards and provides business insights from deal and work order data. The system fetches live data, cleans it, analyzes metrics, and answers natural language questions about business performance.

---

## Live Demo

Deployed Application

https://monday-insight-agent.onrender.com



---

## Features

- AI-powered natural language query analysis
- Integration with monday.com API
- Automated data cleaning and preprocessing
- Business insight generation
- Pipeline and deal analytics
- Work order performance tracking
- Tool trace logging for debugging
- Web interface for interactive queries

---

## Project Structure

```
Monday-Insight-Agent
│
├── agent
│   ├── ai_agent.py
│   └── query_parser.py
│
├── services
│   ├── monday_api.py
│   ├── data_cleaner.py
│   └── insight_engine.py
│
├── tools
│   ├── get_deals.py
│   └── get_work_orders.py
│
├── utils
│   └── tool_trace.py
│
├── static
│   ├── script.js
│   └── style.css
│
├── templates
│   └── index.html
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Tech Stack

Backend
- Python
- Flask

APIs
- monday.com GraphQL API

AI
- Large Language Model based query analysis

Frontend
- HTML
- CSS
- JavaScript

Deployment
- Render

---

## Installation (Local Setup)

Clone the repository

```
git clone https://github.com/aswanikrsh/Monday-Insight-Agent.git
cd Monday-Insight-Agent
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Create `.env` file in the root folder

```
MONDAY_API_KEY=your_monday_api_key
OPENAI_API_KEY=your_openai_api_key
DEALS_BOARD_ID=your_deals_board_id
WORK_ORDERS_BOARD_ID=your_work_orders_board_id
```

Run the application

```
python app.py
```

Open browser

```
http://localhost:5000
```

---

## Example Queries

Users can ask questions like:

- How many deals are in the energy sector?
- What is the total pipeline value?
- Which sector generates the highest revenue?
- How many deals converted into work orders?
- What is the win rate of our deals?

---

## Deployment

This project is deployed using Render.

Steps used for deployment

1. Push project to GitHub
2. Connect the repository to Render
3. Configure environment variables
4. Set the build command

```
pip install -r requirements.txt
```

5. Set the start command

```
python app.py
```

---

## Author

Aswanikrishna

GitHub Profile  
https://github.com/aswanikrsh

---

## License

This project is created for educational and demonstration purposes.