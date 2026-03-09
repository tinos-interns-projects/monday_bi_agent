from services.monday_api import fetch_board
from config import WORK_ORDERS_BOARD_ID
from utils.tool_trace import add_trace

def get_work_orders():

    add_trace("Fetching Work Orders board")

    data = fetch_board(WORK_ORDERS_BOARD_ID)

    items = data["data"]["boards"][0]["items_page"]["items"]

    orders = []

    for item in items:

        row = {"name": item["name"]}

        for col in item["column_values"]:
            row[col["column"]["title"]] = col["text"]

        orders.append(row)

    return orders