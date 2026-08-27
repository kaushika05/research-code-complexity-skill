import csv

def figure_values(path):
    totals = {}
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["include"] == "yes":
                totals.setdefault(row["condition"], []).append(float(row["response_ms"]))
    return {key: sum(values) / len(values) for key, values in totals.items()}
