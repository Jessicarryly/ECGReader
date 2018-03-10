from datetime import datetime, timedelta
from Parsing import ecg_parser
from Parsing.ParseError import ParseError
from Analyser.tag_searching import search, display_search_result
from Analyser.heart_rate import get_heart_rate_data, compute_mean_heart_rate, find_min_max


def parse_date():
    """
    This function ask the user to write the date for the capture.
    Will loop until good answer is given
    :return: the date as a datetime object
    """
    print("Type Date of the recording start. Format :  \"dd/mm/yy  HH:MM\"")
    raw = input()
    try:
        date = datetime.strptime(raw, "%d/%m/%y %H:%M")
    except ValueError as instance:
        print("Incorrect time/date >" + str(instance))
        return parse_date()
    return date


def main():
    """
    Entry point
    Will call as a script all the program functionality
    - Ask the path for the CSV
    - Ask the date
    - Parse the CSV
    - Look for defined tags
    - Compute heart-rate values (avg, min, max)
    """
    print(
        """
Hello
Please provide the path of the EGC CSV file :
        """)
    path = input()
    date = parse_date()
    print("\nProcessing ...\n")
    try:
        entries = ecg_parser.parse_csv(path)
    except FileNotFoundError:
        print("The given path does not match any file")
        return
    except ParseError as instance:
        print(instance)
        return

    tag_search_result = search(entries, ["P", "QRS"], ["premature"])
    display_search_result(tag_search_result)

    rate_data = get_heart_rate_data(entries)
    mean_rate = compute_mean_heart_rate(rate_data)
    print("The mean heart rate of the record is " + str(mean_rate) + " QRS complexes appearance / minute\n")

    min_max = find_min_max(rate_data)
    date_min = date + timedelta(minutes=min_max["max_time"])
    date_max = date + timedelta(minutes=min_max["min_time"])
    print("The minimum heart rate was " + str(min_max["min"]) + " and occurred the " + str(date_min))
    print("The maximum heart rate was " + str(min_max["max"]) + " and occurred the " + str(date_max))

if __name__ == "__main__":
    main()
