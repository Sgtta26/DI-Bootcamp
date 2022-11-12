import enchant


class AnagramChecker:

    LANG = "en_US"
    WORDS_FILE = "sowpods.txt"

    def __init__(self):
        self.check_word = enchant.Dict(self.LANG).check
        with open(self.WORDS_FILE, "r") as f:
            self.words = f.read().split("\n")

    def is_valid_word(self, word):
        return self.check_word(word)

    @staticmethod
    def is_anagram(word1, word2):
        word1, word2 = word1.lower(), word2.lower()
        return sorted(word1) == sorted(word2)

    def get_anagrams(self, search_word):
        search_word = search_word.upper()
        if not self.is_valid_word(search_word):
            return None

        res = [word for word in self.words if self.is_anagram(search_word, word)]
        if res:
            res.remove(search_word)
        return res


def main():
    anagram_checker = AnagramChecker()
    word = "MEAT"
    print(anagram_checker.get_anagrams(word))


if __name__ == "__main__":
    main()
