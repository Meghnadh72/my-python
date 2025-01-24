def mergeAlternately(self, word1: str, word2: str) -> str:
    alternate_word = ""
    bigger_word = word1 if len(word1) > len(word2) else word2
    try:
        for index, letter in enumerate(word1):
            alternate_word += word1[index]
            alternate_word += word2[index]
    except IndexError:
        alternate_word += bigger_word[index + 1 :]
        return alternate_word
    if len(word2) > index:
        alternate_word += bigger_word[index + 1 :]
        return alternate_word
