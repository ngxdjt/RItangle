import itertools

toA = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}

# either abs(toA - toA) or 26 - abs(toA - toA)

def pathLength(word:list):
    total = 0

    for n in range(len(word)-1):
        if abs(toA[word[n]] - toA[word[n+1]]) > 26 - abs(toA[word[n]] - toA[word[n+1]]):
            total += 26 - abs(toA[word[n]] - toA[word[n+1]])
        else:
            total += abs(toA[word[n]] - toA[word[n+1]])
    
    return total

permutations = list(itertools.permutations(["r","i","t","a","n","g","l","e"]))

pathLengths = []
for permutation in permutations:
    pathLengths.append(pathLength(permutation))
pathLengths.sort()
print(pathLengths[0] * pathLengths[-1])