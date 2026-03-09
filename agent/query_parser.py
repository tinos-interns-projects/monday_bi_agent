def parse_query(query):

    q = query.lower()

    result = {}

    # ----------------------
    # PIPELINE QUESTIONS
    # ----------------------
    if "pipeline" in q or "total pipeline" in q or "pipeline value" in q:
        result["intent"] = "pipeline"

    # ----------------------
    # DEAL COUNT QUESTIONS
    # ----------------------
    elif "how many deals" in q or "total deals" in q or "number of deals" in q:
        result["intent"] = "pipeline"

    # ----------------------
    # SECTOR QUESTIONS
    # ----------------------
    elif "sector" in q or "industry" in q:
        result["intent"] = "sector_analysis"

    # ----------------------
    # OWNER QUESTIONS
    # ----------------------
    elif "owner" in q or "sales" in q:
        result["intent"] = "owner_analysis"

    # ----------------------
    # WORK ORDER QUESTIONS
    # ----------------------
    elif "work order" in q or "workorder" in q or "order status" in q:
        result["intent"] = "workorder_analysis"

    return result