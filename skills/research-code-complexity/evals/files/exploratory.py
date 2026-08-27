rows = [1, 2, None, 4]
clean = []
for row in rows:
    if row is not None:
        if row > 0:
            clean.append(row)
print(sum(clean) / len(clean))
