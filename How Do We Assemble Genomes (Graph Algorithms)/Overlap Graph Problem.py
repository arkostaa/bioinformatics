def input_custom_patterns():
    custom_patterns = []
    while True:
        try:
            pattern = input()
            if pattern == '':
                break
            custom_patterns.append(pattern)
        except:
            break
    return custom_patterns

custom_patterns = input_custom_patterns()

for i in range(len(custom_patterns)):
    for j in range(len(custom_patterns)):
        if custom_patterns[i][1:] == custom_patterns[j][:-1] and i != j:
            print(custom_patterns[i] + ' -> ' + custom_patterns[j])

