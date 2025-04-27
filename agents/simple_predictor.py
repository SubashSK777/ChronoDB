def make_prediction(data: str) -> str:
    if "good" in data.lower():
        return "The future looks promising!"
    elif "bad" in data.lower():
        return "Prepare for challenges ahead."
    else:
        return "Future trends are neutral."
