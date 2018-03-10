
def get_heart_rate_data(entries):
    """
    Will go through  a list of @Entry, look for the QRS tag and count how many QRS Entries in a the same minute
    :param entries: List of @Entry
    :return: a List, index are minutes and values are QRS reps.
    """
    data = [0] * (int(entries[-1].onset / (1000 * 60)) + 1)
    for entry in entries:
        if entry.type == "QRS":
            minute = int(entry.onset / (1000 * 60))
            data[minute] += 1
    return data


def compute_mean_heart_rate(rate_data):
    """
    Compute the average heart rate of the record
    :param rate_data:  a List, index are minutes and values are QRS reps.
    :return: the average QRS reps for a minute
    """
    return int(sum(rate_data) / len(rate_data))


def find_min_max(rate_data):
    """
    Go through a list of heart rate where index are minutes and values are QRS reps.
    Look for the min and max
    :return: A dict with the min and max value, and the associated minutes
    """
    current_min = rate_data[0]
    current_time_min = 0
    current_max = rate_data[0]
    current_time_max = 0

    for minute, entry in enumerate(rate_data):
        if entry < current_min:
            current_min = entry
            current_time_min = minute
        if entry > current_max:
            current_max = entry
            current_time_max = minute

    return {"min": current_min, "min_time": current_time_min, "max": current_max, "max_time": current_time_max}
