from services.monday_api import fetch_board
from config import DEALS_BOARD_ID
from utils.tool_trace import add_trace

def get_deals():

    add_trace("Fetching Deals board")

    data = fetch_board(DEALS_BOARD_ID)

    items = data["data"]["boards"][0]["items_page"]["items"]

    deals = []

    for item in items:

        row = {"name": item["name"]}

        for col in item["column_values"]:
            row[col["column"]["title"]] = col["text"]

        deals.append(row)

    return deals