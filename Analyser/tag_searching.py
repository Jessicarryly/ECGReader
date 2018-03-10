def search(entries, types, tags):
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
    for wave_types, tags in results.items():
        print("For the wave type " + wave_types + " :")
        for tag, occurrences in tags.items():
            print("     There is " + str(occurrences) + " occurrences tagged \'" + tag + "\'")
    print("\n")
