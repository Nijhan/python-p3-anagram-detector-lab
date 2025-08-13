# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        """Return a list of anagrams from candidates."""
        sorted_word = sorted(self.word)
        return [c for c in candidates if sorted(c.lower()) == sorted_word and c.lower() != self.word]
