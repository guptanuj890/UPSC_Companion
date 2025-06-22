def classify_topic(summary):
    if "parliament" in summary.lower():
        return "Polity"
    elif "economy" in summary.lower():
        return "Economy"
    else:
        return "General Studies"
