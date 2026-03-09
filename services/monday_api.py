import requests
from config import MONDAY_API_KEY
from utils.tool_trace import add_trace

url = "https://api.monday.com/v2"

headers = {
    "Authorization": MONDAY_API_KEY
}


def fetch_board(board_id):

    add_trace(f"Calling Monday API for board {board_id}")

    # Validate board_id
    if not board_id:
        add_trace("Error: board_id is missing")
        return {}

    query = f"""
    {{
      boards(ids: {board_id}) {{
        items_page(limit:100) {{
          items {{
            name
            column_values {{
              text
              column {{
                title
              }}
            }}
          }}
        }}
      }}
    }}
    """

    try:

        response = requests.post(
            url,
            json={"query": query},
            headers=headers,
            timeout=20
        )

        # Check HTTP errors
        response.raise_for_status()

        data = response.json()

        # Check GraphQL errors
        if "errors" in data:
            add_trace(f"Monday API Error: {data['errors']}")
            return {}

        add_trace("Monday API response received")

        return data

    except requests.exceptions.Timeout:
        add_trace("Monday API request timed out")
        return {}

    except requests.exceptions.RequestException as e:
        add_trace(f"Monday API request failed: {str(e)}")
        return {}

    except Exception as e:
        add_trace(f"Unexpected error: {str(e)}")
        return {}