def string_from_genome_path(patterns):
    reconstructed_string = patterns[0]
    k = len(patterns[0])
    for pattern in patterns[1:]:
        reconstructed_string += pattern[-1]
    return reconstructed_string

input_patterns = []

while True:
    try:
        pattern = input()
        if pattern == '':
            break
        input_patterns.append(pattern)
    except:
        break


result = string_from_genome_path(input_patterns)
print(result)
