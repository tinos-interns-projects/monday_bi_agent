from agent.query_parser import parse_query
from tools.get_deals import get_deals
from tools.get_work_orders import get_work_orders
from services.insight_engine import (
    pipeline_health,
    sector_analysis,
    owner_analysis,
    workorder_analysis
)
from utils.tool_trace import add_trace


def handle_query(query):

    add_trace("Understanding user query")

    parsed = parse_query(query)

    intent = parsed.get("intent")

    add_trace(f"Detected intent: {intent}")

    # Fetch live data
    add_trace("Fetching Deals board")
    deals = get_deals()

    add_trace("Fetching Work Orders board")
    work_orders = get_work_orders()

    # -------------------------
    # PIPELINE
    # -------------------------
    if intent == "pipeline":

        result = pipeline_health(deals)

        total = result["total_pipeline_value"]
        count = result["deal_count"]

        return f"""
Pipeline Health Summary

Total Pipeline Value: ${total:,.2f}
Total Deals: {count}
"""

    # -------------------------
    # SECTOR ANALYSIS
    # -------------------------
    elif intent == "sector_analysis":

        result = sector_analysis(deals)

        if not result:
            return "No sector data available."

        output = "Sector Performance\n\n"

        for sector, count in result.items():
            output += f"{sector}: {count} deals\n"

        return output

    # -------------------------
    # OWNER ANALYSIS
    # -------------------------
    elif intent == "owner_analysis":

        result = owner_analysis(deals)

        if not result:
            return "No owner data available."

        output = "Owner Performance\n\n"

        for owner, count in result.items():
            output += f"{owner}: {count} deals\n"

        return output

    # -------------------------
    # WORK ORDER ANALYSIS
    # -------------------------
    elif intent == "workorder_analysis":

        result = workorder_analysis(work_orders)

        if not result:
            return "No work order data available."

        output = "Work Order Status\n\n"

        for status, count in result.items():
            output += f"{status}: {count}\n"

        return output

    # -------------------------
    # DEFAULT RESPONSE
    # -------------------------
    else:

        return """
I couldn't understand the question.

Try asking:

• How is our pipeline?
• Which sector has most deals?
• Who owns the most deals?
• Show work order status
"""