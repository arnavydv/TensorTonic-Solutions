from collections import Counter

def mean_median_mode(x: list) -> dict:
    mean_val = sum(x) / len(x)
    sorted_x = sorted(x)
    n = len(sorted_x)
    if n % 2 == 1:
        median_val = sorted_x[n // 2]
    else:
        median_val = (sorted_x[(n // 2) - 1] + sorted_x[n // 2]) / 2
    counts = Counter(sorted_x)
    mode_val = counts.most_common(1)[0][0] 
    return {
        "mean": float(mean_val),
        "median": float(median_val),
        "mode": float(mode_val)
    }
