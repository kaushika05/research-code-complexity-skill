"""Archived with the paper; canonical reproduction script, frozen."""
def reproduce(records):
    kept = []
    for row in records:
        if row["eligible"] and not row["withdrawn"]:
            if row["score"] is not None:
                kept.append(row["score"])
    return sum(kept) / len(kept)
