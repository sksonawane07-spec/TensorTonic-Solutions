def min_max_scaling(data: list) -> list:
    column = list(zip(*data))
    minimums = [min(col) for col in column]
    maximums = [max(col) for col in column]

    result = []
    for row in data:
        scaled_data = []
        for j in range(len(row)):
            minimum = minimums[j]
            maximum = maximums[j]

            if maximum == minimum:
                value = 0.0

            else:
                value = (row[j] - minimum)/(maximum - minimum)
            scaled_data.append(value)
        result.append(scaled_data)
    return result