from anagram_checker import AnagramChecker


def validate_word(word):
    word = word.strip()
    if len(word.split(" ")) != 1:
        raise Exception("Only a single word is allowed.")
    return word


def main():
    anagram_checker = AnagramChecker()
    while True:
        print(("1. Choose word for anagrams\n" "2. For exit type -1\n"))
        word = input("")
        if word == "-1":
            return

        word = validate_word(word)

        anagrams = anagram_checker.get_anagrams(word)
        if anagrams == None:
            print("Word not valid")
            continue
        print(anagrams)


main()
