# put your python code here
def hamming_distance(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count


def median_string(k, DNA):
    min_distance = float('inf')
    min_pattern = ""

    for i in range(4**k):
        pattern = ""
        index = i
        for j in range(k):
            pattern = "ACGT"[index % 4] + pattern
            index //= 4

        total_distance = 0
        for DNA_string in DNA:
            min_DNA_distance = float('inf')
            for j in range(len(DNA_string) - k + 1):
                DNA_kmer = DNA_string[j:j+k]
                distance = hamming_distance(pattern, DNA_kmer)
                min_DNA_distance = min(min_DNA_distance, distance)
            total_distance += min_DNA_distance

        if total_distance < min_distance:
            min_distance = total_distance
            min_pattern = pattern

    return min_pattern


k = int(input())
DNA = []
str_input = " "
while str_input != "":
    try:
        str_input = input()
        DNA.append(str_input)
    except:
        break
result = median_string(k, DNA)
print(result)



