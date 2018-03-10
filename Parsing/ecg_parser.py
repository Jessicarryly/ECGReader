import csv

from DataStructure.Entry import Entry
from Parsing.ParseError import ParseError


def parse_csv(path):
    """
    Load the CSV file from the given path, and parse it into a list of @Entry
    :param path: Path of the CSV
    :return: List of Entry
    """
    entries = []
    with open(path) as ecg_data:
        ecg_reader = csv.reader(ecg_data, delimiter=",")
        for row in ecg_reader:
            try:
                entry = Entry(row[0], int(row[1]), int(row[2]), row[3:])
            except ValueError as instance:
                raise ParseError(str(instance))
            entries.append(entry)
    return entries

