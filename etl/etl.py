def transform(legacy_data):
    unsorted = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            unsorted[letter.lower()] = score
    # Sorting the dictionary.
    result = {}
    for letter in sorted(unsorted.keys()):
        result[letter] = unsorted[letter]
    return result
