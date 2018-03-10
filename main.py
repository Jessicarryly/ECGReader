from datetime import datetime
from Parsing import ecg_parser
from Parsing.ParseError import ParseError
from Analyser.tag_searching import search, display_search_result
from Analyser.heart_rate import get_heart_rate_data, compute_mean_heart_rate


def parse_date():
    print("Type Date of the recording start. Format :  \"dd/mm/yy  HH:MM\"")
    raw = input()
    try:
        date = datetime.strptime(raw, "%d/%m/%y %H:%M")
    except ValueError as instance :
        print("Incorrect time/date >" + str(instance))
        return parse_date()
    return date


def main():
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
    print("The mean heart rate of the record is " + str(mean_rate) + " QRS complexes appearance / minute")


if __name__ == "__main__":
    main()
