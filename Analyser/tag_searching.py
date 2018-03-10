def search(entries, types, tags):
    """
    Look for given tags in given entries
    :param entries: A list of Entry
    :param types: a list of types to filter in the entries list
    :param tags: a List of tag to search
    :return: a dict with the types, tags and number of occurrence
    """
    results = {}
    for wave_type in types:
        results[wave_type] = {}
        for tag in tags:
            results[wave_type][tag] = 0
    for entry in entries:
        if entry.type in types:
            for tag in tags:
                if entry.is_tagged_with(tag):
                    results[entry.type][tag] += 1
    return results


def display_search_result(results):
    """
    Pretty print the result of the search function
    :param results: return value of search function
    :return: Nothing
    """
    for wave_types, tags in results.items():
        print("For the wave type " + wave_types + " :")
        for tag, occurrences in tags.items():
            print("     There is " + str(occurrences) + " occurrences tagged \'" + tag + "\'")
    print("\n")
