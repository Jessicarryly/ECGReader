
def get_heart_rate_data(entries):
    data = [0] * (int(entries[-1].onset / (1000 * 60)) + 1)
    for entry in entries:
        if entry.type == "QRS":
            minute = int(entry.onset / (1000 * 60))
            data[minute] += 1
    return data


def compute_mean_heart_rate(rate_data):
    return int(sum(rate_data) / len(rate_data))

