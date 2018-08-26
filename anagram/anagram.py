#done with 2 functions
def is_anagram(word, candidate):

    word = word.lower()
    candidate = candidate.lower()

    return word != candidate and sorted(word) == sorted(candidate)

def test1(word, candidates):
    return [candidate for candidate in candidates if is_anagram(word, candidate)]


#done with Counter
import collections as col

def detect_anagrams(word, tab):
    chars = col.Counter(word.lower())
    return [candy for candy in tab if chars == col.Counter(candy.lower()) and candy.lower() != word.lower()]

#done with for loops (tons of code)
def test3(word, candidates):
    word = word.lower()
    winners = []
    top_dog = []

    for i in range(len(candidates)):

        if word == candidates[i].lower():
            continue

        winners.append(candidates[i])
        candidates[i] = list(candidates[i].lower())

        if len(word) != len (candidates[i]):
            continue

        for letter in word:
            if letter in candidates[i]:
                candidates[i].remove(letter)

        if len(candidates[i]) == 0:
            top_dog.append(winners[i])

    return top_dog
