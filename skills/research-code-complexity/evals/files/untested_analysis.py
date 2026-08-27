def summarize(records, policy):
    selected = []
    for record in records:
        if policy == "strict":
            if record["complete"] and record["quality"] > 0.9:
                selected.append(record)
        elif policy == "lenient":
            if record["quality"] > 0.5:
                selected.append(record)
        else:
            if record["complete"]:
                selected.append(record)
    return {"count": len(selected), "mean": sum(row["value"] for row in selected) / len(selected)}
