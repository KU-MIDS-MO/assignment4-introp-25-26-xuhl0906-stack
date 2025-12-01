import numpy as np

def mask_and_classify_scores(arr):
    if not isinstance(arr, np.ndarray):
        return None
    if arr.ndim != 2:
        return None
    if arr.shape[0] != arr.shape[1]:
        return None
    if arr.shape[0] < 4:
        return None

    n = arr.shape[0]

  
    cleaned = arr.copy()
    for i in range(n):
        for j in range(n):
            if cleaned[i, j] < 0:
                cleaned[i, j] = 0
            elif cleaned[i, j] > 100:
                cleaned[i, j] = 100


    levels = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            val = cleaned[i, j]
            if val < 40:
                levels[i, j] = 0
            elif val < 70:
                levels[i, j] = 1
            else:
                levels[i, j] = 2


    row_pass_counts = np.zeros(n, dtype=int)
    for i in range(n):
        count = 0
        for j in range(n):
            if cleaned[i, j] >= 50:
                count += 1
        row_pass_counts[i] = count

    return cleaned, levels, row_pass_counts

