"""Literal transcription of synthetic paper Equation 7; operation order is intentional."""

def equation_7(x, regime, boundary):
    total = 0.0
    for value in x:
        if regime == "subcritical":
            if value < boundary:
                total += value * value
            else:
                total += boundary * value
        elif regime == "critical":
            if value == boundary:
                total += 0.5 * value
            elif value < boundary:
                total += value
            else:
                total -= value - boundary
        else:
            if value <= 0:
                continue
            total += (value - boundary) * (value + boundary)
    return total
