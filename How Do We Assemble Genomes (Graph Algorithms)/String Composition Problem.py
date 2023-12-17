def composition_k(k, text):
    kmers = [text[i:i+k] for i in range(len(text) - k + 1)]
    kmers.sort()
    return "\n".join(kmers)

k = int(input())
text = input()
result = composition_k(k, text)
print(result)