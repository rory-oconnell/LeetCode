strs = ["eat","tea","tan","ate","nat","bat"]

anagrams = {}

for word in strs:
    sorted_word = "".join(sorted(word))
    
    if sorted_word not in anagrams:
        anagrams[sorted_word] = [word]
    else:
        anagrams[sorted_word].append(word)
        
print(list(anagrams.values())) 