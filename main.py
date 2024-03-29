def decode(input_file):
    # Opening file
    with open(input_file, "r") as f:
        data = f.readlines()

    # Inserting data from file into array
    word_dict = {int(line.split()[0]): line.split()[1] for line in data}

    # Sorting array in ascending order
    sorted_index = sorted(word_dict.keys())

    # i for iteration, p_level for pyramid level
    message = []
    i, p_level = 0, 0

    # Getting result
    while i < len(sorted_index):
        message.append(word_dict[sorted_index[i]])
        p_level += 1
        i += p_level + 1

    # Return result
    return ' '.join(message)  # Remove trailing space


if __name__ == '__main__':
    # First test output from task
    print(decode("./input.txt"))
    # Second output from task
    print(decode("./coding_qual_input.txt"))


