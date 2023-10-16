def makeAnagram(a, b):
    dict1 = {}
    dict2 = {}
    deletions = 0

    for i in range(len(a)):
        if a[i] in dict1:
            dict1[a[i]] += 1
        else:
            dict1[a[i]] = 1

    for j in range(len(b)):
        if b[j] in dict2:
            dict2[b[j]] += 1
        else:
            dict2[b[j]] = 1

    for k in range(len(a)):
        if a[k] not in dict2:
            del dict1[a[k]]
            deletions += 1

    for m in range(len(b)):
        if b[m] not in dict1:
            del dict2[b[m]]
            deletions += 1

    return deletions

if __name__ == "__main__":
    a = "fcrxzwscanmligyxyvym"
    b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"

    res = makeAnagram(a,b)
    print(res)
