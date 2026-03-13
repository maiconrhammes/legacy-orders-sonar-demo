def normalize_text(value):
    result = value.strip()
    result = result.lower()
    result = result.replace("  ", " ")
    return result

def classify_total(total):
    if total > 1000:
        return "high"
    elif total > 500:
        return "medium"
    elif total > 100:
        return "low"
    elif total > 50:
        return "low"
    else:
        return "very_low"
