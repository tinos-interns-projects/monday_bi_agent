from services.data_cleaner import clean_currency
from utils.tool_trace import add_trace


# ------------------------------
# PIPELINE HEALTH
# ------------------------------
def pipeline_health(deals):

    add_trace("Running pipeline health analysis")

    total = 0
    count = 0

    for deal in deals:

        for key, value in deal.items():

            if "value" in key.lower() or "amount" in key.lower():

                cleaned = clean_currency(value)

                total += cleaned
                count += 1

    return {
        "total_pipeline_value": total,
        "deal_count": count
    }


# ------------------------------
# SECTOR ANALYSIS
# ------------------------------
def sector_analysis(deals):

    add_trace("Running sector analysis")

    sector_counts = {}

    for deal in deals:

        for key, value in deal.items():

            if "sector" in key.lower():

                sector = value if value else "Unknown"

                sector_counts[sector] = sector_counts.get(sector, 0) + 1

    return sector_counts


# ------------------------------
# OWNER ANALYSIS
# ------------------------------
def owner_analysis(deals):

    add_trace("Running owner analysis")

    owner_counts = {}

    for deal in deals:

        for key, value in deal.items():

            if "owner" in key.lower():

                owner = value if value else "Unknown"

                owner_counts[owner] = owner_counts.get(owner, 0) + 1

    return owner_counts


# ------------------------------
# WORK ORDER ANALYSIS
# ------------------------------
def workorder_analysis(work_orders):

    add_trace("Running work order analysis")

    status_counts = {}

    for order in work_orders:

        for key, value in order.items():

            if "status" in key.lower():

                status = value if value else "Unknown"

                status_counts[status] = status_counts.get(status, 0) + 1

    return status_counts