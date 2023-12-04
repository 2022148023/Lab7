with open("input_7_2.txt") as file:
    occurrences = {}
    # read lines
    for line in file.readlines():
        for char in line:
            # check if character is an alphabet
            if char.isalpha():
                alphabet = char.upper()
                # add to dict
                if alphabet in occurrences:
                    occurrences[alphabet] += 1
                else:
                    occurrences[alphabet] = 0
    # transform to list
    alphabet_list = []
    for alphabet, occurrence in occurrences.items():
        alphabet_list.append((occurrence, alphabet))
    # sort list and output
    alphabet_list.sort(reverse=True)
    output_list = []
    for alphabet in alphabet_list:
        output_list.append(alphabet[1])
    print(output_list)
