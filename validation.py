import random


class WordValidator:
    def __init__(self):
        self.words = []

    def load_words(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                cleaned_word = line.strip()
                self.words.append(cleaned_word)

    def get_random_word(self):
        words_length = len(self.words)
        random_num = random.randrange(0, words_length)
        return self.words[random_num]

    def validate_word(self, word):
        return word.lower() in self.words

    def __repr__(self):
        return f"{self.words}\n"
